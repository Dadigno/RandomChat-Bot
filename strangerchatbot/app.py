import db as DB
import bot
import time
from Log.logger import log
import config as conf

if __name__ == "__main__":
    log("Init app")
    DB.connect()
    bot.run()
    
    while 1:
        time.sleep(1)
        