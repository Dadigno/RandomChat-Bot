-- DROP TABLE IF EXISTS Users;
CREATE TABLE IF NOT EXISTS Users (
  id          BIGINT UNIQUE,
  name        TEXT NOT NULL,
  type        TEXT NOT NULL,
  banned      BOOLEAN DEFAULT FALSE,
  timestamp timestamp default current_timestamp,
  PRIMARY KEY (id)
);

-- DROP TABLE IF EXISTS Rooms;
CREATE TABLE IF NOT EXISTS Rooms (
  id          BIGINT UNIQUE,
  room        INT NOT NULL,
  PRIMARY KEY (id)
);

CREATE FUNCTION join_room(chat_id BIGINT, r INT)
RETURNS INT AS $$
DECLARE ret INT := -1;
BEGIN
    IF  (SELECT count(*) FROM Rooms WHERE room = r) = 0 OR 
        (SELECT count(*) FROM Rooms WHERE room = r) < 2 THEN 
            INSERT INTO Rooms (id,room) VALUES(chat_id,r); 
            ret = r;
    END IF; 
    RETURN ret;
END;
$$  LANGUAGE plpgsql