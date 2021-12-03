# -*- coding: utf-8 -*-

import scripts.reg_my_cmd as reg
import Util
import DiscordHelper
import random

# Main
def lambda_handler(event, context):
    # print(f"event {event}") # debug print
    
    util = Util.Util() # helps data parsing & storage works
    
    ### after update cmd, register cmd to discord ###
    # It is not intended to do so everytime a lambda is invoked
    # comment out this line for general chat bot usage
    # return reg.run()
    
    # verify the signature in incoming request
    util.verify_request(event)

    # get command context
    cmd_ctx = util.get_cmd_cxt(event)
    
    # record command
    util.record_cmd(cmd_ctx)
    
    # let a helper deals with interaction with Discord
    dch = DiscordHelper.DiscordHelper(cmd_ctx)
    
    # bot responses according to cmd text
    cmd = cmd_ctx.input_text
    
    # start game server
    if cmd == "start":
        dch.reply_quick()
        msg = util.start_game_server()
        dch.reply_with_edited_msg(msg)
        
    # instructions to user with /help command.
    elif cmd == "help":
        msg = util.get_help_text()
        dch.reply_with_msg(msg)
        
    elif cmd == "touch":
        # response: Displeased
        if random.randint(0, 2) == 0:
            url = 'https://i.pinimg.com/originals/84/00/a8/8400a84fe12c730f3b568458c1469a1a.jpg'
            dch.reply_with_url(url)
        else:
            msg = "*Giggle*"
        dch.reply_with_msg(msg)
        
    elif cmd == "toss":
        # 0: just do it; # 1: no just don't
        coin = {
            0 : "https://i.imgur.com/UTTGe94.png", 
            1 : 'https://i.imgur.com/bBt0cBp.jpg'
        }
        index = random.randint(0, 1)
        url = coin[index]
        dch.reply_with_url(url)
        
    # display particular info
    elif cmd == "show":
        opts = event.get('body-json').get("data").get("options")[0]
        opt_name= opts.get("name")
        
        if opt_name == "rule":
            opt_val = opts.get("value")
            
            if opt_val == "rule_mc_server":
                msg = util.get_rule_mc_server()
                    
            elif opt_val == "rule_chat_bot":
                msg = util.get_rule_chat_bot()
                
            else:
                msg = f"I don\'t know this rule {opt_val}"
        
        dch.reply_with_msg(msg)
        
    elif cmd == "meme":
        url = util.get_meme_pic()
        dch.reply_with_url(url)
        
    elif cmd == "time":
        msg = util.get_current_time()
        dch.reply_with_msg(msg)
        
    elif cmd == "gm":
        msg = "Good morning!"
        dch.reply_with_msg(msg)
        
    elif cmd == "gn":
        msg = "Good night!"
        dch.reply_with_msg(msg)
        
    elif cmd == "ping":
        msg = "PONG!"
        dch.reply_with_msg(msg)
        
    elif cmd == "testing":
        msg = "You know this is testing!"
        dch.reply_with_msg(msg)
        
    else:
        msg = f'I don\'t understand... Maybe try the help at /help'
        dch.reply_with_msg(msg)
        
