
## Prerequisites
* A Discord account + token key + bot settings
* AWS EC2 (Linux + t3.micro)
* Node JS ^14
  * discord js ^12
  * request js ^2 (optional)

## Create bot on AWS EC2
* Login the machine
* Follow these steps
```
$ curl -sL https://rpm.nodesource.com/setup_14.x | sudo bash -
$ yum install -y nodejs
$ (opt.) node --version
$ (opt.) npm --version
$
$ mkdir -p /var/discord-bot
$ cd /var/discord-bot
$ npm init -y
$
$ # installing a well known Javascript library for interacting with Discord API 
$ npm install --save discord.js
$ 
$ # create your bot
$
$ # check your bot is working via discord
$ 
$ # make service which could be started automatically (as below)
```
* [package.json](https://github.com/MOHOAzure/Discord-chat-bot/blob/main/EC2/package.json)

* [auth.json](https://github.com/MOHOAzure/Discord-chat-bot/blob/main/EC2/auth.json)

* [server_config.json](https://github.com/MOHOAzure/Discord-chat-bot/blob/main/EC2/server_config.json)

* [Bot code](https://github.com/MOHOAzure/Discord-chat-bot/blob/main/EC2/bot.js)


## Run bot the host machine is started
* [chatbot.service](https://github.com/MOHOAzure/Discord-chat-bot/blob/main/EC2/chatbot.service)

* Add user to manage the auto service
```
$ groupadd -r chatbot
$ useradd -r -g chatbot -d "/var/chatbot" -s "/bin/bash" chatbot
$ chown minecraft.minecraft -R /var/chatbot/
$ 
$ # create a system service file, the content is presented in the following section
$ nano /etc/systemd/system/chatbot.service
$ 
$ chmod 644 /etc/systemd/system/chatbot.service
$ systemctl daemon-reload
$ systemctl enable chatbot
$ 
$ # manully check service could be started
$ systemctl start chatbot
$ systemctl status chatbot -l
$ systemctl stop chatbot
$
$ # after the host machine is re-started, the service would be on-line
```

## Ref
* Creating your first Discord Bot — Part 1, Renemari Padillo, https://medium.com/davao-js/2019-tutorial-creating-your-first-simple-discord-bot-47fc836a170b
* [Discord JS offical doc](https://discordjs.guide/popular-topics/embeds.html#embed-preview)
* How to Install Node.js and npm on CentOS 7, https://linuxize.com/post/how-to-install-node-js-on-centos-7/

