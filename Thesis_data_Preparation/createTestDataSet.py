#!/usr/bin/python
# Author : Hasan
import csv
import re
import sys


fileName  = sys.argv[1];

sys.stdout.write("Month_w0,Dist_to_Stream,Dist_to_Border,Rainfall_w0,NDVI_w0,Malaria_w0,Month_w1,Rainfall_w1,NDVI_w1,Malaria_w1,Month_w2,Rainfall_w2,NDVI_w2,Malaria_w2,Month_w3,Rainfall_w3,NDVI_w3,Malaria_w3,Slope,Stream_Density\n");
star = "*";
with open(fileName, 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        sys.stdout.write(row[0]+","+row[1]+","+row[2]+","+row[3]+","+
        	row[4]+","+row[5]+","+row[6]+","+star+","+star+","+star+","+
        	row[10]+","+star+","+star+","+star+","+row[14]+","+star+","+star+","+star+","+row[18]+","+row[19]+"\n");
    sys.stdout.flush();    
