
#!/usr/bin/python
# --------------------------------------------------------------------

import numpy as np
import pandas as pd
import mysql.connector
import sys

from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob

# --------------------------------------------------------------------

# Open database connection
db = mysql.connector.connect(
    user='root',
    password='root',
    host='localhost',
    database='db',
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

# --------------------------------------------------------------------

# execute the SQL query using execute() method.
cursor.execute("select complaint from complaintform")

data = cursor.fetchall()
# print(data)

# --------------------------------------------------------------------

with open('dataset.csv', 'r') as fp:
    classifier = NaiveBayesClassifier(fp, format="csv")

for row in data:
    # print(row)
    blob = TextBlob(str(row), classifier=classifier)
    prob = blob.classify()
    # print(prob)
    pr = "neg"
    status = "HIGH"
    # st = str(row)
    # print(row)
    print(prob)
    if prob == pr:
        # if 3 < 9:
        # print(prob)
        stmt = "UPDATE complaintform SET priority ='HIGH' where complaint='%s'" % (row)
        cursor.execute(stmt)

        db.commit()
        # print("Row(s) were updated : " + str(cursor.rowcount))

# cursor.execute(sql)
# # Commit your changes in the database
# db.commit()

# except:
# Rollback in case there is any error
#    db.rollback()

# --------------------------------------------------------------------

# disconnect from server
db.close()