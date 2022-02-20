# Changelog for Scanner

## 02/20/2022 06:24
Working on a function to run async w/ the backend_main function to allow for the adding of stocks. Ultimately calls on add_update_stock, but allows for a csv file to passed as input as well. When the backend_main is run, this function should run concurrently, allowing for the adding of stocks via the command line while the backend_main function performs the necessary checks and calls. 

- Complete writing new add function
- Write test for add function with a lot of different things to test.
- Remove the early return after creating the database in backend_main.
- Write logic in the if __name__ == "__main__" block to allow for user input of stock info (maybe a third function?)

## 02/19/2022 12:23
Started working on the backend_main file. Hasn't been test-run yet, and I will probably try to first step through with the debugger to make sure everything is working the way it should first. I'll need to modify the date/hour variables to get it to work the way I need it to in testing (likely not a formal test). Once it is working, I will move the backend files to a subfolder, create a dockerfile for it, create a docker-compose file (for the database), and then attempt to deploy to a Raspberry Pi prior to building the dashboard.

Next steps:
- Change Day/Hour vars as needed for testing at any time.
- Step through, make sure data is recorded as needed.
- Move to subfolder
- Create Dockerfile
- Create Docker-compose file
- Figure out how to regularly backup a docker volume to an external drive?

### 18:39
Ran into a KeyError on a symbol when fetching new info. Need to build a more robust test on the get info function to ensure that all fields are present, and if not present, then None. The rest of the backend_main function seems to be working okay though.

### 19:36
Created a new test to check for missing variables from the yf call and fill them in as None. Updated the get_stock_info file to accommadate for this. The symbols currently in the database all wrote successfully.

### 21:25
Realizing the way my backend_main function is written may not be ideal. It would probably be better to write the function with the weekday/hour logic *outside* of the function itself, especially as the function is currently set to connect to and call to the database when it's run, so effectively, it's a loop of calls to the database. Given the small scale of the project, it probably won't be an issue, but I should probably fix it anyway. Not a high priority right now.

## 02/13/2022 07:15
Something about not failing, just finding a million ways that didn't work. get_stock_info passes the test, granted, with some try/except logic, only for datatype conversion though (as the values being pulled from the DB were Decimals and not floats, except when they were strings or None). Might be able to start building the main part of the script now? At least a functional loop to regularly pull info after market close.

### 07:55
Adding a new function that tests to see if the tables exist in the database. Need to build the test for it.

### 08:02
New function check_db passes a basic test. Now onwards to sketching out (by hand, in onenote) the main script, then implementing.

## 02/12/2022 08:10
Continuing to get the `Instance is not bound to a session` error. Tried changing a few things but the error persists. Next thing I'll try is just using my connect() function to get the engine object and using engine.connect(), instead of the session() that I'd normally use. Not sure if this is how select statements work with SQLalchemy? I'm half tempted to just write the whole thing using raw SQL.

### 15:40
Identified error that will cause the tests to fail when I stop getting tracebacks: the data type for query[k] is a Decimal object, whereas data[v] is a float. I need to find a way to convert this decimal object to a float in this comparison. And fix the Key errors. There's that too. **CAUSE**: the revenue_growth key error is due to an extra space at the end of the name. That needs fixed.

## 02/08/2022 06:39
Built a test for adding new stock info to the database. First error is in the function itself, it gets a data error, integer out of range. Need to research how to update the columns in these tables to have the highest data precision. Possibly changing all values in that table to type Numeric.

### 06:56
Test still fails, but now at a different point. Currently getting a `Instance is not bound to a session` error. However, the data did sucessfully write to the database, but now we just need to be sure that we can check that data against a pull from yf at about the same time. Also updated the StockInfo columns to type `Numeric` and fixed a datetime issue in `add_update_stock`.

## 02/04/2022 06:08
Testing the add_update_stock function. Fails the test, but it did successfully add the entry to the database. Now I just need to write in the update logic, and then it will hopefully pass the test. 

### 16:26

Datetime records to the database in the correct timezone (mine) now. Not doing much more to ensure UTC time writing/conversion, etc. as I'm the only targeted user.

Updated add_update_stock passes test.

### 06:49
After some slight trouble with almost accidentally corrupting the database (really just needed to restart the container), the add_update_stock function passes the test. However, the datetime_updated column in the database is recording the time as if my timezone is UTC + 5, instead of minus. I'm not sure exactly what's going on here, or what will be involved in fixing it.

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