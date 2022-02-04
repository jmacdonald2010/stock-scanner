# Changelog for Scanner

## 02/03/2022 22:48
Got the Database build script to work and fully build the database after having quite the time getting docker to run the container. 

Currently working on the add_update_stock script. Working to add in the logic to get the industry/sector ids for adding/updating stocks. Working to keep as many of the functions in separate files as possible to keep things as clean as possible.

Things that need done:
- Probably some arguments for the database connection scripts.
- Need to check to see how the add vs update functionality works when adding/updating stocks, as I'm not terribly familiar with SQLalchemy.
- Probably hide the old notebooks into some folder targeted by gitignore to clean up the repository.
- Yes I know my db password is publicly visible, I'm not terribly worried since I'm not planning on taking this DB live on the internet and there is also no sensitive information that will be stored in it.

## 02/01/2022 21:42
Realizing now that if I want to multithread/async the get data/write data portion of the script, I won't really be able to reliably use sqllite, so I guess I'll need to get a docker postgres container running, along with the appropriate schema, etc.

To do: Postgresql Docker container, change sqlalchemy things to work w/ it

### 21:59
Also think I need to move the classes for the tables into separate files to load into the main file. The Build DB file can still have a function present that builds the database.