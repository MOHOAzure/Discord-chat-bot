# -*- coding: utf-8 -*-

class RequestModel:
    # request from chat
    def __init__(self, guild_id, sender_id, sender_name, input_text, interaction_id, interaction_token):
        self.guild_id = guild_id
        self.sender_id = sender_id
        self.sender_name = sender_name
        self.input_text = input_text # command is in here
        self.interaction_id = interaction_id
        self.interaction_token = interaction_token
        
    def __str__(self):
        print(f'guild_id {self.guild_id}')
        print(f'sender_id {self.sender_id}')
        print(f'sender_name {self.sender_name}')
        print(f'input_text {self.input_text}')
        print(f'interaction_id {self.interaction_id}')
        print(f'interaction_token{self.interaction_token}')
        
