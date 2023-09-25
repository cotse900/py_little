#  update the cell in pandas df
df.loc[row, [column]] = value

#one way to iterate through a dataframe

#first establish the first column to iterate through
    working_column = [name]
    #Have for loop that goes through all the columns
    for column in range(0,(df.shape[1])):
    #check if the column exists
        if working_column in df:
    #THEN go into for loop going down through all rows in that column
            for row in range(0, (df.shape[0])):

#get cell contents

contents = DF.iloc[row][column]

#Get column names as a list:
You can get the column names from pandas DataFrame using df. columns. values , and pass this to python list() function to get it as list,

#connect to a postgreSQL db
#Need to install library in the terminal (use either of the two commands below)
pip install psycopg2
pip3 install psycopg2-binary 

import psycopg2
import pandas as pd

conn = psycopg2.connect(
    database="DVDRental",
    user="postgres",
    password="123456",
    host="127.0.0.1",
    port="5432"
)

sql_query = 'SELECT * FROM actor'

# Execute the query and read the results into a DataFrame
df_sql = pd.read_sql_query(sql_query, conn)

print(df_sql)
