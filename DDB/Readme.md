# DynamoDB Setup
  
| Field Name    | Type          | Note |
| ------------- | ------------- | ------------- |
| datetime      | string        | Partition key; The time when a message is sent to the bot |
| sender_id     | string        | Sort key; The ID of Discord user who sends the message |
| guild_id      | string        | The ID of Discord chatroom (channel) where the message is sent |
| input_text    | string        | Message content |
| sender_name   | string        | The user name of Discord user who sends the message |
