# Changelog for Scanner

## 02/01/2022 21:42
Realizing now that if I want to multithread/async the get data/write data portion of the script, I won't really be able to reliably use sqllite, so I guess I'll need to get a docker postgres container running, along with the appropriate schema, etc.

To do: Postgresql Docker container, change sqlalchemy things to work w/ it

### 21:59
Also think I need to move the classes for the tables into separate files to load into the main file. The Build DB file can still have a function present that builds the database.