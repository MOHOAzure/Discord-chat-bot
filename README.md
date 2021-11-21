# Discord-chat-bot
A chat bot working on Discord. The bot is established on AWS services.

# Prerequisites
* A Discord account + token key + bot settings
* AWS EC2 (Linux + t3.micro)
* Node JS ^14
  * discord js ^12
  * request js ^2 (optional)

# Discord settings
* Login https://discordapp.com/developers/applications/
* New application named `discord-bot`
* Add bot
* Reveal bot token key and copy it
* Auth bot (Follow least privilege discipline)
  * Go to `OAuth2` inside app page
  * In panel `scopes`, select `bot`
  * In panel `bot permission`, select `Send Messages` and `Read Message History`
  * copy & paste the generated auth link to a new browser tab
  * add the bot to a server (create a server if needed)

# Create bot on AWS
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
$ # create your bot (example code below)
$
$ # check your bot is working
$ 
$ # make service which could be started automatically (as below)
```

* Bot code
```
const Discord = require('discord.js');
const client = new Discord.Client();
const auth = require('./auth.json');
const server_config = require('./server_config.json');
var request = require('request');

client.login(auth.key);

client.on('ready', ()=> {
        console.log(`logged in as ${client.user.tag}!`);
});

client.on('message', msg=> {
        if(msg.content === '/ping') {
                msg.reply('Pong!');
        }
        else if(msg.content === '/start') {
                url = server_config.mc_endpoint;

                request(url, function (error, response, body) {
                  console.log('error:', error);
                  console.log('statusCode:', response && response.statusCode);
                  console.log('body:', body);
                  msg.reply(body);
                });
        }
});
```

* auth.json
```
{
  "key":"DISCORD_TOKEN_KEY"
}
```

* server_config.json
```
{
  "mc_endpoint": "API_TO_START_SERVER"
}
```

# Run bot without screen
* Run bot when the host machine is started
* chatbot.service
```
[Unit]
Description=Chatbot Server
Wants=network.target
After=network.target

[Service]
User=chatbot
Group=chatbot
Nice=5
KillMode=control-group
SuccessExitStatus=0 1

ProtectHome=true
ProtectSystem=full
PrivateDevices=true
NoNewPrivileges=true
PrivateTmp=true
InaccessibleDirectories=/root /sys /srv -/opt /media -/lost+found
ReadWriteDirectories=/var/discord-bot
WorkingDirectory=/var/discord-bot
ExecStart=/bin/node bot.js

[Install]
WantedBy=multi-user.target
```

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

# Ref
* Creating your first Discord Bot — Part 1, Renemari Padillo, https://medium.com/davao-js/2019-tutorial-creating-your-first-simple-discord-bot-47fc836a170b
* https://linuxize.com/post/how-to-install-node-js-on-centos-7/
