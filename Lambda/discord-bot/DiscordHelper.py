# -*- coding: utf-8 -*-

import json
import random
import requests
from datetime import datetime
import my_config

class DiscordHelper:
    def __init__(self, cmd_ctx):
        # Discord rely on URL to send response message
        # Ref: https://discord.com/developers/docs/interactions/receiving-and-responding#followup-messages
        self._url_for_response = f"https://discord.com/api/v8/interactions/{cmd_ctx.interaction_id}/{cmd_ctx.interaction_token}/callback" # post
        self._url_for_response_edit = f"https://discord.com/api/webhooks/{my_config.APPLICATION_ID}/{cmd_ctx.interaction_token}/messages/@original" # edit preivous message sent by bot # patch
        # self._url_for_response_followup = f"https://discord.com/api/webhooks/{my_config.APPLICATION_ID}/{cmd_ctx.interaction_token}" # send a follow-up message by replying to bot itself # post
    
    
    def __str__(self):
        pass
    
    
    # Send a quick response to Discord since Discord requires init response within 3 sec
    # Ref: https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-response-object-interaction-callback-data-structure
    # Because of Discord slash command, it takes longer than 3 sec for Discord to receive a response when conducting another web API, start_game_server(), though the API responsed less than 1 sec
    # Therefore, a simple message is sent to Discord as init response
    def reply_quick(self):
        msg = 'Roger that!'
        self.reply_with_msg(msg)
        
        # This is useful for debug
        # json = {
        #     "type": my_config.INTERACTION_TYPE['MESSAGE_WITH_SOURCE'],
        #     "data": {
        #         "content": msg
        #     }
        # }
        # try:
        #     r = requests.post(self._url_for_response, json=json)
        # except Exception as e:
        #     raise Exception(f"Exception: {e}")
    
    
    # this one is used after reply_quick() when this chat bot need more than 3 sec to interact with Discord
    def reply_with_edited_msg(self, msg):
        # simple ver but ugly
        json = {
            "type": my_config.INTERACTION_TYPE['MESSAGE_WITH_SOURCE'],
            "content": msg
        }
        
        # # If payload json is any one of the following, Discord report Unknown interaction (10062) & Unknown Webhook (10015)
        
        # json = {
        #     "type": my_config.INTERACTION_TYPE['MESSAGE_WITH_SOURCE'],
        #     "content": msg,
        #     "data": {
        #         "embeds": [{
        #             "description": msg,
        #             "color": "3066993"
        #         }]
        #     }
        # }
        
        # json = {
        #     "type": my_config.INTERACTION_TYPE['MESSAGE_WITH_SOURCE'],
        #     "data": {
        #         "content": "",
        #         "embeds": [{
        #             "description": msg,
        #             "color": "3066993"
        #         }]
        #     }
        # }
        
        # json = {
        #     "type": my_config.INTERACTION_TYPE['MESSAGE_WITH_SOURCE'],
        #     "embeds": [{
        #         "description": msg,
        #         "color": "3066993"
        #     }]
        # }
        
        try:
            r = requests.patch(self._url_for_response_edit, json=json)
            print(r.text)
        except Exception as e:
            raise Exception(f"Exception: {e}")
    
    
    def reply_with_msg(self, msg):
        json = {
            "type": my_config.INTERACTION_TYPE['MESSAGE_WITH_SOURCE'],
            "data": {
                "embeds": [{
                    "description": msg,
                    "color": "3066993"
                }],
            }
        }
        try:
            r = requests.post(self._url_for_response, json=json)
            print(r.text)
        except Exception as e:
            raise Exception(f"Exception: {e}")
    
    
    def reply_with_url(self, url):
        json = {
            "type": my_config.INTERACTION_TYPE['MESSAGE_WITH_SOURCE'],
            "data": {
                "tts": False,
                "content": "",
                "embeds": [{
                    "url": url,
                    "thumbnail": {"url": url},
                    "color": "2067276"
                }],
                "allowed_mentions": []
            }
        }
        try:
            r = requests.post(self._url_for_response, json=json)
            print(r.text)
        except Exception as e:
            raise Exception(f"Exception: {e}")
    
