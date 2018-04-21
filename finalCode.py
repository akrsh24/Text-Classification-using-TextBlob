#!/usr/bin/python
# --------------------------------------------------------------------

import numpy as np
import pandas as pd
import mysql.connector
import sys
import csv
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

# --------------------------------------------------------------------

with open('data.csv', 'r') as fp:

    classifier = NaiveBayesClassifier(fp, format="csv")
    
for row in data:
    # print(row)
    blob = TextBlob("No water supply", classifier=classifier)
    prob = blob.classify()
    pr = "neg"
    status = "HIGH"
    print(row)  
    print(prob)
    # if prob == pr:
    #     stmt = "UPDATE complaintform SET priority ='HIGH' where complaint='%s'" % (
    #         row)
    #     cursor.execute(stmt)

    # else:
    #     stmt = "UPDATE complaintform SET priority ='LOW' where complaint='%s'" % (
    #         row)
    #     cursor.execute(stmt)
        
    db.commit()
    # print("Row(s) were updated : " + str(cursor.rowcount))

    classifier.show_informative_features(5)

    # csvRow = ''.join(row)
    # print(csvRow)
    # fields = [csvRow, prob]
    # with open(r'dataset_test.csv', 'a') as f:
    #    writer = csv.writer(f)
    #    writer.writerow(fields)

# --------------------------------------------------------------------

# disconnect from server
db.close()
