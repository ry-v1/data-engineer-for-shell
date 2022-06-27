# Project: Data Modeling with Postgres


### Purpose of this project 

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. 

The analytics team is particularly interested in understanding what songs users are listening to.


### How to run the Python scripts

Execute the python files from the command

e.g. >> python create_table.py


### About the files in the repository

  - sql_queries.py
      
    This file has DDL and DML commands to create the fact and dimension tables.
  
  - create_tables.py
  
    This file creates/closes the database connections and creates and drop the tables.
    
  - etl.ipynb
    
    This jupyter notebook helps in exploring the input data and create the required tables.
  
  - etl.py
  
    This file processes the input data((songs, log) files and creates the fact and dimension tables which helps in the analysis.
  
  - test.ipynb

    This jupyter notebook does the sanity testing for the datamodel designed.
    

### State and justify your database schema design and ETL pipeline.

As Sparkify analytics team wants to understand what songs users are listening to, created a fact table ***songplays*** with the songs users are listening from the log file. Along with the ***songs, artists, users, time*** as dimensions tables.

ETL pipeline reads the songs, log JSON files and transforms into the tables based on the data model defined for the analysis.


### Example queries and results for song play analysis.

Refer to analysis.ipnyb