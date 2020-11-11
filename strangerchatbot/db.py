import os
from Log.logger import *
import psycopg2
import config as conf
import time

params = {
    'database': 'botDb',
    'user': 'admin',
    'password': 'admin',
    'host': 'strangerchat_postgres_1',
    'port': 5432
    }

SELECT_USERS = "SELECT * FROM Users"
SELECT_ROOMS = "SELECT * FROM Rooms"
SELECT_PARTNER = "SELECT id FROM Rooms WHERE room = (SELECT room FROM Rooms WHERE id = %s) and id != %s;"
INSERT_USER = "INSERT INTO Users (id, name, type) VALUES(%s, %s, %s);"
CHECK_JOIN = "SELECT * FROM Rooms WHERE id = %s"
CHECK_USER = "SELECT name FROM Users WHERE id = %s"
CHECK_BAN = "SELECT * FROM Users WHERE id = %s and banned = true"
JOIN_ROOM = "SELECT join_room(%s,%s);"
LEAVE_ROOM = "DELETE FROM Rooms WHERE id = %s"
BAN_USER = "UPDATE Users SET banned = %s WHERE id = %s"

global connection 

def connect():

    global connection 
    try:
        connection = psycopg2.connect(**params)
        connection.set_session(autocommit=True)
        log("Database connected")
    except  (Exception, psycopg2.DatabaseError) as error:
        log("Error in database connection")
        all_exception_handler()
    
    query(INSERT_USER,(conf.ID_ADMIN,'Admin','Admin'))

    

def query(q,arg = ()):
    result = None
    try:
        with connection.cursor() as cursor:
            cursor.execute(q,arg)
            result = cursor.fetchall()
    except psycopg2.ProgrammingError as error:
        if error == 'no results to fetch':
            pass
    except  (Exception, psycopg2.DatabaseError) as error:
        all_exception_handler()
    finally:
        if result is None or result == []:
            return False
    return result

#####################
#       UTILS        #
#####################
def join_room(chat_id):
    for room in range(1,20):
        r = query(JOIN_ROOM,(chat_id,room))
        if r != -1:
            return True
    return False


def leave_room(chat_id):
    return query(LEAVE_ROOM,(chat_id,))

def check_join(chat_id):
    return query(CHECK_JOIN,(chat_id,))

def get_partner_by_id(chat_id):
    return query(SELECT_PARTNER,(chat_id,chat_id))