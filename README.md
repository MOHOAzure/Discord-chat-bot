# Discord-chat-bot
* A chat bot working on Discord
* The bot is established on AWS services
  * Two methods are provided (Lambda or EC2)
  
# Background
* [On-Demand-Minecraft-Sever](https://github.com/MOHOAzure/On-Demand-Minecraft-Sever)

# Discord settings
* Login https://discordapp.com/developers/applications/
* New application named `discord-bot`
* Add bot
* Reveal bot token key and copy it
* Auth bot (Follow least privilege discipline)
  * Go to `OAuth2` inside app page
  * In `scopes` panel select `bot permission`, then select `Send Messages` and `Read Message History`
  * In `scopes` panel select `applications.commands`
  * copy & paste the generated auth link to a new browser tab
  * add the bot to a discord server (create a discord server for test if needed)

# Event-trigged with Lambda
* Much cheaper
* Details: https://github.com/MOHOAzure/Discord-chat-bot/tree/main/Lambda
 
# Always running with EC2
* Easy to setup
* Details: https://github.com/MOHOAzure/Discord-chat-bot/tree/main/EC2

# Demo

 ![](https://github.com/MOHOAzure/Discord-chat-bot/blob/main/on%20test%20server.png)
