import os
import glob
import psycopg2
import numpy as np
import pandas as pd
from sql_queries import *

    
def process_song_file(cur, filepath):
    """
    Read JSON file and insert the data into "songs", "artists" tables.
    
    Keyword arguments:
    cur -- database cursor
    filepath -- path to the JSON files
    """
    
    # open song file
    df_song = pd.read_json(filepath, lines=True)
    
    # ADDITIONAL - insert raw song data
    try:
        cur.execute(songs_table_insert, df_song.values[0].tolist())
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error in songs table: %s" % error)
        
    # insert song record
    song_data = df_song[["song_id", "title", "artist_id", "year"
                         , "duration"]].values[0].tolist()
    
    try:
        cur.execute(song_table_insert, song_data)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error in songs table: %s" % error)

    
    # insert artist record
    artist_data = df_song[["artist_id", "artist_name", "artist_location"
                           , "artist_latitude", "artist_longitude"]].values[0].tolist()
    
    try:
        cur.execute(artist_table_insert, artist_data)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error in artists table: %s" % error)


def process_log_file(cur, filepath):
    """
    Read JSON file and inserts the data into "time", "users", and "songplays" tables.
    
    Keyword arguments:
    cur -- database cursor
    filepath -- path to the JSON file
    """
    
    # open log file
    df_log = pd.read_json(filepath, lines=True)
    #print(df_log.columns)
    
    # ADDITIONAL - insert raw log table   
    try:
        cur.executemany(log_table_insert, df_log.values)
    except (Exception, psycopg2.Error) as error:
        print("Error in Time table: %s" % error)
        
    # filter by NextSong action
    df_nextsong = df_log[df_log.page == "NextSong"].dropna()

    # convert timestamp column to datetime
    df_time = df_nextsong.copy()
    df_time.loc[:,"ts"] = pd.to_datetime(df_time["ts"], unit='ms')
    t = pd.to_datetime(df_time["ts"], unit='ms')
    
    # insert time data records
    time_data = list((t, t.dt.hour, t.dt.day, t.dt.week
                      , t.dt.month, t.dt.year, t.dt.weekday))
    #print(time_data)
    
    column_labels = ["start_time", "hour", "day", "week", "month"
                     , "year", "weekday"]
    time_df = pd.DataFrame.from_dict(dict(zip(column_labels, time_data)))
    

    # insert one row at a time
    #
    #for i, row in time_df.iterrows():
    #    try:
    #        cur.execute(time_table_insert, list(row))
    #    except (Exception, psycopg2.DatabaseError) as error:
    #        print("Error in Time table: %s" % error)

    time_tuples = [tuple(x) for x in time_df.values]
    #print(time_tuples)
    
    # insert many rows at a time
    try:
        cur.executemany(time_table_insert, time_df.values)
    except (Exception, psycopg2.Error) as error:
        print("Error in Time table: %s" % error)
    
    # load user table
    user_df = df_nextsong[["userId", "firstName", "lastName", "gender"
                           , "level"]].drop_duplicates(subset=["userId"], inplace=False)

    # insert user records one row at a time
    #for i, row in user_df.iterrows():
    #    try:
    #        cur.execute(user_table_insert, row)
    #    except (Exception, psycopg2.DatabaseError) as error:
    #        print("Error in User table: %s" % error)

    # insert many rows at a time
    try:
        cur.executemany(user_table_insert, user_df.values)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error in User table: %s" % error)
        
    # insert songplay records
    for index, row in df_time.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = (row.ts, row.userId, row.level, songid, artistid, row.sessionId
                         , row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    """
    Read JSON file and inserts the data into "time", "users", and "songplays" tables.
    
    Keyword arguments:
    cur -- database cursor
    conn -- database connection
    filepath -- path to the JSON files
    func -- function used to process the JSON files
    """
    
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()