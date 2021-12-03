# -*- coding: utf-8 -*-

import my_config
import boto3
import requests
import json
import random
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError
from datetime import datetime
from models import RequestModel

class Util:
    def __init__(self):
        pass
    
    
    def __str__(self):
        pass
    
        
    # verify each request from remote
    def verify_request(self, event):
        try:
            raw_body = event.get("rawBody")
            auth_sig = event['params']['header'].get('x-signature-ed25519')
            auth_ts  = event['params']['header'].get('x-signature-timestamp')
            
            message = auth_ts.encode() + raw_body.encode()
            verify_key = VerifyKey(bytes.fromhex(my_config.APPLICATION_PUBLIC_KEY))
            verify_key.verify(message, bytes.fromhex(auth_sig)) # raises an error if unequal
        except BadSignatureError as e:
            raise Exception(f"[UNAUTHORIZED] Invalid request signature: {e}")
        except Exception as e:
            raise Exception(f"Exception: {e}")


    # get command context
    def get_cmd_cxt(self, event):
        body = event.get('body-json')
        input_text = body.get("data").get("name")
        guild_id = body.get("guild_id")
        sender_id = body.get("member").get("user").get("id")
        sender_name = body.get("member").get("user").get("username")
        interaction_id = body.get("id")
        interaction_token = body.get("token")
        
        cmd_cxt = RequestModel.RequestModel(guild_id, sender_id, sender_name, input_text, interaction_id, interaction_token)
        
        return cmd_cxt
        

    # record command from user
    def record_cmd(self, cmd_cxt):
        # print("DB")
        # print(cmd_cxt.__str__())
        table = boto3.resource("dynamodb").Table(my_config.DDB_NAME)
        response = table.put_item(
            Item={
                "datetime": datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S"),
                "sender_id": cmd_cxt.sender_id,
                "sender_name": cmd_cxt.sender_name,
                "guild_id": cmd_cxt.guild_id,
                "input_text": cmd_cxt.input_text,
            }
        )


    # start game server (EC2)
    def start_game_server(self):
        try:
            r = requests.get(my_config.GAME_SERVER_TRIGGER)
            if r.status_code == requests.codes.ok:
                return r.text
            else:
                print(f'Unexpected status from game server : {r.status}')
        except Exception as e:
            print(e)
    
    
    # TODO: get a meme from internet
    def get_meme_pic(self):
        try:
            file_data = 'https://i.imgur.com/IUzlrAc.jpeg'
            return file_data
        except Exception as e:
            print(e)
    
    
    def get_help_text(self):
        # load commands from json file
        commands = None
        with open('scripts/commands.json') as json_file:
            commands = json.load(json_file)
            
        if not commands:
            msg = "No command is available"
        else:
            msg = "The following commands are available:\n\n"
            for command in commands:
                msg += f"/{command['name']:8} : {command['description']}\n"
        return msg
    
    
    def get_rule_mc_server(self):
        msg = "Participants obey the following rules:\n\n"
        for k, r in my_config.RULE_MC_SERVER.items():
            msg += f"{k:3}: {r}\n\n"
        return msg
        
        
    def get_rule_chat_bot(self):
        msg = "About Prushka:\n\n"
        for k, r in my_config.RULE_CHAT_BOT.items():
            msg += f"{k:3}: {r}\n\n"
        return msg
        
    def get_current_time(self):
        current_time = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
        msg = f"Right now its {current_time} UTC."
        return msg
