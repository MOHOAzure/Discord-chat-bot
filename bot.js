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
        if(msg.content === '/start') {
                url = server_config.mc_trigger;

                request(url, function (error, response, body) {
                  console.log('error:', error);
                  console.log('statusCode:', response && response.statusCode);
                  console.log('body:', body);

                  var message = new Discord.MessageEmbed()
                        .setDescription(body)
                        .setColor("#5865F2")
                  msg.reply(message);
                });
        }

        else if(msg.content === '/ping') {
                msg.reply('Pong!');
        }

        else if(msg.content === '/touch') {
          if(msg.author.id == server_config.special_user){
                var message = new Discord.MessageEmbed()
                .setColor("#2ECC71")
                .setDescription("Ha Ha!");
                msg.reply(message);
          }
          else {
                msg.reply("Giggle");
          }
        }

        else if(msg.content === '!touch') {
                msg.reply('BONK!');
        }
});
