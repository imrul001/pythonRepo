#!/usr/bin/python
#Author : Hasan

import csv
import re

def check_sp_uniref90(row):
	if row[2] == '\.' and row[3]!= '\.':
		return True;
    elif: row[7] == '\.' and row[8]!= '\.':
    	return True;
    else:
        return False;	


with open('c01_trinotate_annotation_report_e_default.xls', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    for row in reader:
        flag = check_sp_uniref90(row);
        if flag == True:
            # print tid+'\t'+str(description);
            print "\t".join(row);
            break;