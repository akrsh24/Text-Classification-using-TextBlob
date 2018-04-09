#!/usr/bin/python
# --------------------------------------------------------------------

import numpy as np
import pandas as pd
import mysql.connector
import sys
from mysql.connector.cursor import MySQLCursorPrepared

from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob