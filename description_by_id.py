#!/usr/bin/python
#Author : Hasan

import csv
import re

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1;

def search_id(file_name,id):
    with open(file_name, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        result = "";
        i=0;
        for row in reader:
            if id == row[0]:
                if i == 0:
                    result=row[1]+row[2];
                    i=i+1;
                else:
                    result=result+row[1]+row[2];
                    i=i+1;
    if i == 0:
        return  None;
    else:
        return result;


length=file_len("20150128_c01_Trinity_BLASTN_UNIQ.fasta.lngth");
tid=range(length);

with open('20150128_c01_Trinity_BLASTN_UNIQ.fasta.lngth', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    print '#query_id'+'\t'+'Description';
    for row in reader:
        tid=row[0];
        description = search_id('check_mapping_id.py.out',tid);
        if description is not None:
            print tid+'\t'+str(description);

            