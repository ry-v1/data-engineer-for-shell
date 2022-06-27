# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"
# addtional tables
log_table_drop = "DROP TABLE IF EXISTS log_data;"
songs_table_drop = "DROP TABLE IF EXISTS song_data;"


# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays
    (
        songplay_id SERIAL PRIMARY KEY, 
        start_time TIMESTAMP NOT NULL, 
        user_id int NOT NULL,
        level varchar, 
        song_id varchar, 
        artist_id varchar, 
        session_id int, 
        location varchar, 
        user_agent varchar
    );
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users
    (
        user_id int PRIMARY KEY, 
        first_name varchar,
        last_name varchar, 
        gender char(1), 
        level varchar
    );
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs
    (
        song_id varchar PRIMARY KEY,
        title varchar NOT NULL, 
        artist_id varchar,
        year int, 
        duration float NOT NULL
    );
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists
    (
        artist_id varchar PRIMARY KEY, 
        name varchar NOT NULL, 
        location varchar, 
        latitude float, 
        longitude float
    );
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time
    (
        start_time timestamp PRIMARY KEY,
        hour int, 
        day int, 
        week int, 
        month int, 
        year int, 
        weekday int
    );
""")

# addtional tables creation
songs_table_create = (""" 
CREATE TABLE IF NOT EXISTS "song_data" (
"artist_id" VARCHAR,
  "artist_latitude" FLOAT,
  "artist_location" VARCHAR,
  "artist_longitude" FLOAT,
  "artist_name" TEXT,
  "duration" FLOAT,
  "num_songs" INTEGER,
  "song_id" VARCHAR,
  "title" VARCHAR,
  "year" INTEGER
);
"""
);

log_table_create = ("""
CREATE TABLE IF NOT EXISTS "log_data" (
"artist" TEXT,
  "auth" TEXT,
  "firstName" TEXT,
  "gender" TEXT,
  "itemInSession" INTEGER,
  "lastName" TEXT,
  "length" FLOAT,
  "level" TEXT,
  "location" TEXT,
  "method" TEXT,
  "page" TEXT,
  "registration" FLOAT,
  "sessionId" INTEGER,
  "song" TEXT,
  "status" INTEGER,
  "ts" BIGINT,
  "userAgent" TEXT,
  "userId" TEXT
)
"""
);

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT(songplay_id) DO NOTHING;
""")

user_table_insert = ("""
    INSERT INTO users (user_id, first_name, last_name, gender, level)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT(user_id) DO NOTHING;
""")

song_table_insert = ("""
    INSERT INTO songs (song_id, title, artist_id, year, duration)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT(song_id) DO NOTHING;
""")

artist_table_insert = ("""
    INSERT INTO artists (artist_id, name, location, latitude, longitude)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT(artist_id) DO NOTHING;
""")

time_table_insert = ("""
    INSERT INTO time (start_time, hour, day, week, month, year, weekday)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT(start_time) DO NOTHING;
""")

# addtional insert statements
songs_table_insert = ("""
    INSERT INTO song_data (artist_id, artist_latitude, artist_location, artist_longitude
    , artist_name, duration, num_songs, song_id, title, year)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING;
""")

log_table_insert = ("""
    INSERT INTO log_data (artist, auth, "firstName", gender, "itemInSession", "lastName", length 
    , level, location, method, page, registration, "sessionId", song, status, ts, "userAgent", "userId")
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING;
""")


# FIND SONGS

song_select = ("""
   SELECT songs.song_id, songs.artist_id
   FROM songs JOIN artists ON songs.artist_id = artists.artist_id
   WHERE songs.title = %s
   AND artists.name = %s
   AND songs.duration = %s;
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create
                       , songs_table_create, log_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop
                     , songs_table_drop, log_table_drop]