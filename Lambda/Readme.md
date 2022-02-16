
## Prerequisites
* A Discord account + token key + bot settings
* AWS Lambda + API Gateway
  * Python 3.7
  * Dependency
    * pynacl
    * An EC2 instance to build the dependency in Amazon machine env

## Ref
* Serverless Discord Custom Slash Commands bot with AWS API Gateway and Lambda, helen, https://oozio.medium.com/serverless-discord-bot-55f95f26f743

## Discord setting
* Follow Discord part in the Ref.

## Lambda Config
* APPLICATION_ID (ID of Discord application to which bot belongs)
* APPLICATION_PUBLIC_KEY (key of Discord application )
* BOT_TOKEN (Discord bot token)
* DDB_NAME (store bot actions)
* GUILD_MAIN (Discord guild for user)
* GUILD_TEST (Discord guild for test)
* GAME_SERVER_TRIGGER (API gateway to start game server)

## Lambda Code
* https://github.com/MOHOAzure/Discord-chat-bot/tree/main/Lambda/discord-bot

## Lambda Layer
* To use 3rd-party lib in lambda, you need to Build lib in Amazon machine env, Zip the lib with the env, and then put zipped files to Lambda as a layer
  * [AWS official description](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html)
  * [Practice steps shown on this StackOverflow post](https://stackoverflow.com/questions/57688731/unable-to-import-module-lambda-function-no-module-named-pandas)
* In short 
  * create a dir, named 'python', for building lib and go inside
  * active virtual env
  * install lib
  * zip the whole dir, the virtual env 'should' be included
  * put it to Lambda layer (with aws CLI)
    * `aws lambda publish-layer-version --layer-name pynacl --zip-file fileb://pynacl_layer.zip`

## Create API gateway
* You need to configure API gateway for Discord and bot communication
* This is complicate and screenshots are helpful. See the Ref for details
  * Serverless Discord Custom Slash Commands bot with AWS API Gateway and Lambda, helen, https://oozio.medium.com/serverless-discord-bot-55f95f26f743

## Register Discord slash command
* Slash command make it easy for end user interact with bot
* You need to register a slash command to a Discord server (using web hook) before use the command
* In my exp., it took 20 sec to register the first 5 commmands to a Discord server, then it took about 20 sec to register another one
* I had 10 commands for 2 Discord servers, and I spent 256 sec (4.5 min) for registration
* I use a script on Lambda to help registration
  * it is trigged by Lambda test
