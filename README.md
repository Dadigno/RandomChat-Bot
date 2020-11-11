# RandomChat-Bot
A Telegram bot which is able to connect randomly multiple users creating anonimous chats

## Features
Each user (`ID` and name) is saved in a database at first `/start`

Connect virtually two users anonymously. When `user1` send the `/join` command his `ID` is assigned to a free room. If `user2` is assigned to the same room all messages sent by `user1` is routed to `user2`

Only text and photo can be sent to another users and neither is saved in the database

Rooms are numbered automatically from 0 to 20

Only one `ID` can be admin of the bot: it is specifed in the `config.py` file

Public commands:

- `/join` a room
- `/leave` the actual room
- `/skip` leave the actual room and join another automatically
- `/report` send a message directly to the admin 

