import csv
csv_file = 'RoadAcc_OverSpeed_Data.csv'   # Define the path to your CSV file

import pypyodbc as odbc
# ODBC = Open Database Connectivity

# define the connection parameters
DRIVER_NAME= 'SQL Server'
SERVER_NAME = 'DESKTOP-0BHTSL9\\VATS'
DATABASE_NAME = 'ACCIDENT_DATA'

# Define the connection string
connection_string = f"""
      DRIVER={{{DRIVER_NAME}}};
      SERVER={SERVER_NAME};
      DATABASE={DATABASE_NAME};
      Trust_Connection=yes;
"""


# establish the connection to the database usng odbc library and "connect" function 
# cursor object allows you to execute SQL queries and fetch results from the database.
# printing the connection object useful in debugging purposes.
conn = odbc.connect(connection_string) 
cursor = conn.cursor()
print (conn)


# cursor.execute() method is used to excute SQL queries using a cursor objcet 
# passed the parameter using execute() method i.e , year state count 
cursor.execute('''   
        CREATE TABLE INDIA.AccDueToOverSpeed (
        State_UT VARCHAR(100),
        Year INT,
        Count INT
         )
   '''  ) 
  

# Initialize an empty list to store the rows of the CSV file
rows = []

# CSV = comma seperated file 
# "with"  ensures that the file is properly closed after executing of blocks , even if exception occurs   
# Open the CSV file in read mode(r)
with open(csv_file, 'r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Append the row to the list of rows
        rows.append(row)

 

# Print the rows read from the CSV file
first_row=[]
for i in range(1,len(rows)):
  data=rows[i]
  for j in range(1,len(data)):
    state = data[0] # rows[i][0]
    year= int(rows[0][j])
    count=int(data[j])   # rows[i][j]
    
    #print("         ")
    #print(state,year,count)


    cursor.execute('''
     INSERT INTO INDIA.AccDueToOverSpeed (State_UT,Year,Count)
     VALUES (?,?,?)
     ''', (state,year,count))


conn.commit()
