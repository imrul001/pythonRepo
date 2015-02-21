#!/usr/bin/python
# Author : Hasan
import csv
import re
import sys
import math

#print "imrul is a good boy";
def findManhattanDist(arr1, arr2):
	sum = 0.0;
	for num in range(0,len(arr1)):
		sum = sum + abs(arr1[num] - arr2[num]);
	return sum;

def findEuclidianDist(arr1, arr2):
	sum = 0.0;
	for num in range(0,len(arr1)):
		val = arr1[num] - arr2[num];
		sum = sum + pow(val,2);
	return math.sqrt(sum);	

arr1 = [6,2,5];
arr2 = [5,4,3];

# arr1 = [22,1,42,10];
# arr2 = [20,0,36,8];

print findManhattanDist(arr1, arr2);

print findEuclidianDist(arr1, arr2);
		

	
