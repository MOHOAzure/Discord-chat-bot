# -*- coding: utf-8 -*-

import json
import requests
from time import sleep
import my_config

# Get commands recorded in json file
def get_cmd_json():
    cmd = None
    with open('scripts/commands.json') as json_file:
        cmd = json.load(json_file)
    return cmd


# publish a command to a specified discord server
def publish_command(url, command):
    # For authorization, you can use either your bot token
    HEADERS = {
        "Authorization": f"Bot {my_config.BOT_TOKEN}"
    }
    # # or a client credentials token for your app with the applications.commands.update scope
    # HEADERS = {
    #     "Authorization": "Bearer <my_credentials_token>"
    # }

    r = requests.post(url, headers=HEADERS, json=command)
    if r.status_code != requests.codes.ok:
        print(f"Post to {url} failed; waiting for retry")
        sleep(20) # pinging the endpoint too frequently causes it to fail; wait and retry
        publish_command(url, command)
        
    # debug print
    print(f"Response from {url}, cmd:{command['name']}: {r.text}")


# get all commands from a specified discord server
def get_all_commands(url):
    HEADERS = {
        "Authorization": f"Bot {my_config.BOT_TOKEN}"
    }
    return requests.get(url, headers=HEADERS).json()
        
    
# delete a specified command in discord server by command id (represented in url)
def delete_command(url):
    HEADERS = {
        "Authorization": f"Bot {my_config.BOT_TOKEN}"
    }
    r = requests.delete(url, headers=HEADERS)
    print(r.text)
    

# conduct cmd registration
def run():
    guild_urls = [f"https://discord.com/api/v8/applications/{my_config.APPLICATION_ID}/guilds/{cid}/commands" for cid in my_config.VALID_CHAT_ID]

    # # optional: delete all existing commands to reset to clean state
    # for guild_url in guild_urls:
    #     print(f"try to del cmds from url: {guild_url}")
    #     for command in get_all_commands(guild_url):
    #         delete_command(f"{guild_url}/{command['id']}")
            
    # publish new commands
    for guild_url in guild_urls:
        print(f"try to add cmds to url: {guild_url}")
        for command in get_cmd_json():
            print(f'command: {str(command)}')
            publish_command(guild_url, command)

    # WARNING !!!
    # uncomment to publish globally
    # for command in commands:
    #     publish_command(global_url, command)
    # print(f"{len(commands)} published")
    
    return True
