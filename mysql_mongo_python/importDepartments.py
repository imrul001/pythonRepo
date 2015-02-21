#!/usr/bin/python
# Author; Hasan

import MySQLdb
import pymongo
import datetime
from pymongo import MongoClient


# Open database connection
db = MySQLdb.connect("localhost","root","123imrul","employees" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT * FROM `departments`")

# Fetch a single row using fetchone() method.
client = MongoClient('localhost', 27017);
mongoDB=client.TestMongoDB
collection=mongoDB.departments


rows = cursor.fetchall()

for row in rows:
    departMentInfo={"dept_no":row[0],"dept_name":row[1]}
    collection.insert(departMentInfo)


# disconnect from server
db.close()