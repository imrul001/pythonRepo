#!/usr/bin/python
#Author : Hasan

import csv
import re
import math
import sys

with open('distance.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    sys.stdout.write("Village_id"+"\t"+"Nearest-1"+"\t"+"Nearest-2"+"\t"+"Nearest-3"+"\t"+"Nearest-4"+"\n");
    for row in reader:
    	v_id = row[0];
    	x_coord=float(row[1]);
    	y_coord=float(row[2]);
    	sys.stdout.write(v_id+"\t");
    	with open('distance.csv', 'rb') as csvfile1:
        	reader2 = csv.reader(csvfile1, delimiter='\t')
        	for row1 in reader2:
        		near_village_id = row1[0];
		    	x_coord1=float(row1[1]);
    			y_coord1=float(row1[2]);
    			dist = math.sqrt(math.pow(x_coord-x_coord1,2) + math.pow(y_coord-y_coord1,2));
    			if dist <= 4000 and dist != 0:
    				sys.stdout.write(near_village_id+'\t');
    		sys.stdout.write("\n");

