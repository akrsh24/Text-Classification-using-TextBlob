#!/usr/bin/python
#--------------------------------------------------------------------

import numpy as np
import pandas as pd
import mysql.connector
import sys

from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob

#--------------------------------------------------------------------

# Open database connection
db = mysql.connector.connect(
    user='root',
    password='root',
    host='localhost',
    database='TESTDB',
    buffered=True,
    autocommit=True)

# if (db):
#     # Carry out normal procedure
#     print ("Connection successful")
# else:
#     # Terminate
#     print ("Connection unsuccessful")

# prepare a cursor object using cursor() method
cursor = db.cursor()

#--------------------------------------------------------------------

# execute the SQL query using execute() method.
cursor.execute("select problem from employee")

data = cursor.fetchone()
print(data)

#--------------------------------------------------------------------

with open('dataset.csv', 'r') as fp:

    classifier = NaiveBayesClassifier(fp, format="csv")

blob = TextBlob(str(data), classifier=classifier)
prob = blob.classify()
print(prob)

#--------------------------------------------------------------------

# if blob.classify() == "neg":
# Prepare SQL query to UPDATE required records
#     sql = "UPDATE employee SET priority = 'HIGH'"

# else:
#      sql = "UPDATE EMPLOYEE SET priority = 'LOW'"

# cursor.execute(sql)
#db.commit()

#try:
#curso r = db.cursor()

# Execute the SQL command
# print(blob.classify())
pr="neg"
if prob == pr:
# if 3 < 9:
    print(prob)
    cursor.execute(
        "UPDATE employee SET priority = 'HIGH' where priority = 'LOW'")

    db.commit()
    print("Row(s) were updated : " + str(cursor.rowcount))

# cursor.execute(sql)
# # Commit your changes in the database
# db.commit()

#except:
# Rollback in case there is any error
#    db.rollback()

#--------------------------------------------------------------------

# disconnect from server
db.close()