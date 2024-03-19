import csv
import datetime
from datetime import datetime

# Define the path to your CSV file
csv_file = 'RoadAcc_Road_Injury_Data.csv'

import pypyodbc as odbc

# Define the connection parameters
DRIVER_NAME= 'SQL Server'
SERVER_NAME = 'DESKTOP-0BHTSL9\\VATS'
DATABASE_NAME = 'ACCIDENT_DATA'
username = 'DESKTOP-0BHTSL9\\hp'
password = '8051707627'
#UID={username};
#PWD={password};
# Define the connection string
connection_string = f"""
      DRIVER={{{DRIVER_NAME}}};
      SERVER={SERVER_NAME};
      DATABASE={DATABASE_NAME};
      Trust_Connection=yes;
"""
# Create the database connection
conn = odbc.connect(connection_string)
cursor = conn.cursor()
print (conn)

cursor.execute('''
        CREATE TABLE INDIA.AccidentData (
        State_UT VARCHAR(100),
        Year INT,
        RoadType VARCHAR(50),
        InjuryType VARCHAR(50),
        Count INT
         )
   '''  )
# Initialize an empty list to store the rows of the CSV file
rows = []

# Open the CSV file and read its contents
with open(csv_file, 'r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Append the row to the list of rows
        rows.append(row)
    #print(rows)


# Print the rows read from the CSV file
first_row=[]
for i in range(1,len(rows)):
  data=rows[i] # [1,AndhraPradesh, 13846, 4333,........... ,50000]
  #for(j=2;j<data.length();j++)
  for j in range(2,len(data)):
    variable=rows[0][j].split("-") # [SurfacedRoads,Accidents, 2014]
    road_type=variable[0] # SurfacedRoads
    injury_type=variable[1] # Accidents
    
    # Convert the string to a date object with January 1st of that year
    #date_object = datetime.strptime(variable[2], '1')
    # Extract the year from the date object
    #year = date_object.year
    year=int(variable[2])


    state=data[1]
    count=int(data[j])
    #print (road_type,injury_type,count)
    cursor.execute('''
    INSERT INTO INDIA.AccidentData (State_UT,Year,RoadType,InjuryType,Count)
    VALUES (?,?,?,?,?)
    ''', (state,year,road_type,injury_type,count) )
    

# cursor.execute('SELECT * FROM INDIA.AccidentData')  # Replace YourTableName with the actual table name
#    results = cursor.fetchall()
#    for row in results:
#    print (row)
# Fetch the results from the cursor
conn.commit()






    
