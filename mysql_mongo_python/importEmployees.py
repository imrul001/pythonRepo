#!/usr/bin/python

import MySQLdb
import pymongo
import datetime
from pymongo import MongoClient


# Open database connection
db = MySQLdb.connect("localhost","root","123imrul","employees" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT * FROM `employees`")

# Fetch a single row using fetchone() method.
client = MongoClient('localhost', 27017);
mongoDB=client.TestMongoDB
collection=mongoDB.info


rows = cursor.fetchall()

for row in rows:
    d1=datetime.datetime.strptime(str(row[5]),'%Y-%m-%d');
    d2=datetime.datetime.strptime(str(row[1]),'%Y-%m-%d');
    authorInfo={"emp_no":row[0],"birth_date":d2,"first_name":row[2],"last_name":row[3],"gender":row[4], "hire_date": d1}
    collection.insert(authorInfo)


# disconnect from server
db.close()