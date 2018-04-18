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
    host='127.0.0.1',
    database='db',
    buffered=True,
    autocommit=True)

# prepare a cursor object using cursor() method
cursor = db.cursor()

# --------------------------------------------------------------------

# execute the SQL query using execute() method.
cursor.execute("select complaint from complaintform")

data = cursor.fetchall()


# --------------------------------------------------------------------

with open('dataset.csv', 'r') as fp:

    classifier = NaiveBayesClassifier(fp, format="csv")

# for row in data:

    blob = TextBlob("I am happy", classifier=classifier)
    prob = blob.classify()
    senti = "neg"
    status = "HIGH"

    myFile = open('dataset.csv', 'a')
    newData = [["Problems", "Sentiments"],['I am happy', prob]]
    with myFile:
        writer= csv.writer(myFile)
        writer.writerows(newData)

    # print(row)
    # print(senti)
    # if prob == senti:
    #     # if 3 < 9:
    #     # print(prob)
    #     stmt = "UPDATE complaintform SET priority ='HIGH' where complaint='%s'" % (
    #         row)
    #     cursor.execute(stmt)

    #     db.commit()

    #     print("Row(s) were updated : " + str(cursor.rowcount))

# --------------------------------------------------------------------

# disconnect from server
db.close()
