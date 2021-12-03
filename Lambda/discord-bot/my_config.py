# -*- coding: utf-8 -*-

import os

# discord app key # for verification
APPLICATION_PUBLIC_KEY = os.environ.get("APPLICATION_PUBLIC_KEY")
# check the token is set
if APPLICATION_PUBLIC_KEY is None:
    raise EnvironmentError("Missing APPLICATION_PUBLIC_KEY env variable!")


# app id where bot belongs
APPLICATION_ID = os.environ.get("APPLICATION_ID")

BOT_TOKEN = os.environ.get("BOT_TOKEN")

# chat rooms (guilds) in discord that bot would response
VALID_CHAT_ID = []
VALID_CHAT_ID.append(os.getenv('GUILD_TEST'))
VALID_CHAT_ID.append(os.getenv('GUILD_MAIN'))

# trigger for starting game server
GAME_SERVER_TRIGGER = os.getenv('GAME_SERVER_TRIGGER')

# command description used in the "help" command
# no use for discord bot using slash commands
BOT_COMMANDS = {
    '/start'    : 'Start Game Server',
    '/help'     : 'Gives you information about the available commands',
    '/time'     : 'Tell current time',
    '/GM'       : 'Good morning',
    '/GN'       : 'Good night',
    '/touch'    : 'Show your love',
    '/toss'     : 'Help you make decision'
}

# rules of game server
RULE_MC_SERVER = {
    '1' : '重生點為 0,Y,0 ; Y為該XZ點座標地表',
    '2' : '0, Y,0 各項限延伸100格(+-100, Y, +-100)為共同開發區，建設以公眾導向共同建設，不可聲明主權',
    '3' : '個人建築物含牆等預設距離他人建物距離100格，如經雙方同意則不在此限',
    '4' : '除遇到Server重大故障導致有補償事宜，OP應以生存模式一同參與，不可切至創造模式以及以指令進行遊戲以求公平'
}

# rules of chat bot
RULE_CHAT_BOT = {
    '1' : 'Please treat Prushka warmly',
    '2' : 'Please take her on a thrilling adventure',
    '3' : 'Do not break her into pieces',
}

# REF: https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-object-interaction-type
INTERACTION_TYPE =  { 
    "PONG": 1,
    "MESSAGE_WITH_SOURCE": 4,
}

# bot log
DDB_NAME = os.getenv('DDB_NAME')
