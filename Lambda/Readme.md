
## Prerequisites
* A Discord account + token key + bot settings
* AWS Lambda + API Gateway
* Python 3.7

## Create API gateway
* You need to configure API gateway for Discord and bot communication
* See the following tutorial for details
  * Serverless Discord Custom Slash Commands bot with AWS API Gateway and Lambda, helen, https://oozio.medium.com/serverless-discord-bot-55f95f26f743

## Register Discord slash command
* Slash command make it easy for end user interact with bot
* You need to register a slash command to a Discord server (using web hook) before use the command
* In my exp., it took 20 sec to register the first 5 commmands to a Discord server, then it took about 20 sec to register another one
* I had 10 commands for 2 Discord servers, and I spent 256 sec (4.5 min) for registration
* I use a script on Lambda to help registration
* Details: 

## Create bot on Lambda
* Details: 
