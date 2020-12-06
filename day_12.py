# Create a JSON of all object types and import the JSON into a SQL Database Note: The JSON file should have valus of all Datatypes
import json

# creating JSON file
data = []
data = [
    [
        {"name": "Sandeep", "mark": 100, "grade": "O"},  # dictionary
        [5, 2, 3],  # list
        (3, 2, 1),  # tuple
        "Chennai",  # string
        35,  # integer
        35.5,  # float
        True,  # boolean
        "none"  # none
    ]
]

with open('mydata.json', 'w') as outfile:
    json.dump(data, outfile)
    print("JSON file successfully created")

# JSON file successfully created

import sqlite3

con = sqlite3.connect("test.db")
print("Database successfully connected")

# Database successfully connected

cursor = con.cursor()
try:
    cursor.execute("CREATE TABLE MYDETAILS"
                   "("
                   + "dictinary BLOB,"
                   + "list BLOB,"
                   + "tuple BLOB,"
                   + "string varchar(50),"
                   + "Integer INTEGER,"
                   + "flo FLOAT,"
                   + "Bool BOOLEAN,"
                   + "None BLOB"
                     ");")
except Exception as e:
    print("Error :", e)
else:
    print("Table Successfully created")


# Table Successfully created

datafile = open("mydata.json")
dataset = json.load(datafile)
dataframe = []
for row in dataset:
    data = (str(row[0]), str(row[1]), str(row[2]), str(row[3]), int(row[4]),
            float(row[5]), bool(row[6]), row[7])
    dataframe.append(data)

try:
    cursor.executemany("INSERT INTO MYDETAILS VALUES (?,?,?,?,?,?,?,?)", dataframe)
except Exception as e:
    print("Error : ", e)
else:
    con.commit()
    print("values successfully inserted")

# values successfully inserted

try:
    cursor.execute("SELECT * from MYDETAILS")
except Exception as e:
    print("Error : ", e)
else:
    for row in cursor.fetchall():
        print(row)

con.close()
