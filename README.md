# RandomChat-Bot
A Telegram bot which is able to connect randomly multiple users creating anonimous chats

## Features
Every users (telegram id and name) is saved in a database at his first `/start`
Connect virtually two users anonymously.When two users send the `/join` command their `ID` is saved in the database and the same room is assigned to each of them. 

Rooms are numbered automatically from 0 to 20


Only one `ID` can be admin of the bot: it is specifed in the `config.py` file

Public commands:

- `/join` a room
- `/leave` the actual room
- `/skip` leave the actual room and join another automatically
- `/report` send a message directly to the admin 

