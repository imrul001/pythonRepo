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
cursor.execute("SELECT * FROM `dept_emp`")

# Fetch a single row using fetchone() method.
client = MongoClient('localhost', 27017);
mongoDB=client.TestMongoDB
collection=mongoDB.dept_emp
rows = cursor.fetchall()

for row in rows:
    d2=datetime.datetime.strptime(str(row[2]),'%Y-%m-%d')
    d3=datetime.datetime.strptime(str(row[3]),'%Y-%m-%d')
    departMentInfo={"emp_no": row[0], "dept_no":row[1],"from_date":d2, "to_date": d3}
    collection.insert(departMentInfo)


# disconnect from server
db.close()