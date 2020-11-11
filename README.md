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

Admin commands:
- `/help` list all admin command
- `/alluser` list of all users registered
- `/sendmessage <id> <text>` send a message to a specific `ID`
- `/bad <id>` ban a specific user by his `ID`
- `/unban <id>` unban a specific user by his `ID`
- `/log` get the entire log file of the bot

## Setup and run
Create a bot using [Bot Father](https://telegram.me/BotFather) and get the Token

Modify `config.py` with the admin `ID` and the Token. You can also modify the default name and password of the database in the file `db.py`

Install the last version of docker and docker-compose than build and run the application:

`sudo docker-compose up --build`

You can access the postgres database with

`sudo docker exec -it my_container psql -U admin -W botDb /bin/bash`

my_container is the container ID

## TODO

- Enable other types of messages
- Inline keyboard
- Multi language
- Rooms can support more than two partecipants
- Set name/avar for each user

....what else?


Thanks to [vishnubob](https://github.com/vishnubob) for [wait-for-it](https://github.com/vishnubob/wait-for-it) script






