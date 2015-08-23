#!/usr/bin/python
# Author : Hasan
import csv
import re
import sys


# Method to get previous weeks

def getPreviousWeekRainfall(village_code,currentWeek,fileName):
    with open(fileName,'rb') as cs:
    	reader = csv.reader(cs, delimiter=',')
    	requiredWeek = int(currentWeek) - 1; requiredRainfall = 0;
        for row in reader:
        	if (row[1] ==  village_code and requiredWeek == int(row[0])):
        		requiredRainfall = row[4];
        		break;
    	return requiredRainfall;



sys.stdout.write("Month_w0,village_code,Dist_to_Stream,Dist_to_Border,Rainfall_w-1,Rainfall_w0,NDVI_w0,Malaria_w0,Month_w1,Rainfall_w1,NDVI_w1,Malaria_w1,Month_w2,Rainfall_w2,NDVI_w2,Malaria_w2,Month_w3,Rainfall_w3,NDVI_w3,Malaria_w3,Month_w4,Rainfall_w4,NDVI_w4,Malaria_w4,slope,strm_density\n")
fileName = sys.argv[1];
with open(fileName, 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
    	previousWeeksrainfall = getPreviousWeekRainfall(row[1],row[0],fileName);
        sys.stdout.write(row[0]+","+row[1]+","+row[2]+","+row[3]+","+str(previousWeeksrainfall)+","+
        	row[4]+","+row[5]+","+row[6]+","+row[7]+","+row[8]+","+row[9]+","+
        	row[10]+","+row[11]+","+row[12]+","+row[13]+","+row[14]+","+row[15]+","+row[16]+","+row[17]+","+
        	row[18]+","+row[19]+","+row[20]+","+row[21]+","+row[22]+","+row[23]+","+row[24]+"\n");
    sys.stdout.flush();    