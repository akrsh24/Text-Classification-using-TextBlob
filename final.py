#!/usr/bin/python
#--------------------------------------------------------------------

import numpy as np
import pandas as pd
import mysql.connector

from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob

#--------------------------------------------------------------------

# Open database connection
db=mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='TESTDB')
# prepare a cursor object using cursor() method
cursor = db.cursor()

#--------------------------------------------------------------------

with open('dataset.csv', 'r') as fp:

    classifier = NaiveBayesClassifier(fp, format="csv")

blob=TextBlob('water is coming slow', classifier=classifier)

#--------------------------------------------------------------------


#--------------------------------------------------------------------


if blob.classify( )== "pos" :
# Prepare SQL query to UPDATE required records
    sql ="UPDATE EMPLOYEE SET AGE = AGE + 1 where SEX='M'"

else:
    sql = "UPDATE EMPLOYEE SET AGE = AGE + 2 where SEX='M'"

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()  
except:
   # Rollback in case there is any error
   db.rollback()

#--------------------------------------------------------------------

# disconnect from server
db.close()