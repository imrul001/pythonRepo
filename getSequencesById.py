#!/usr/bin/python
# Author : Hasan
import csv
import re
import sys

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1;

def isTid(line):
    row=line.split();
    id=row[0].split(">");
    return id[1];

length=file_len("check_C1_criteria_false_wssv_false.out");
tid=range(length);
i=0;
with open('check_C1_criteria_false_wssv_false.out', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    for row in reader:
        tid[i]=row[0];
        i=i+1;
values=range(3);
flag = 0;
for num in range(0,length):
    with open('CD_HIT_2_Trinity.fasta', 'rb') as csvfile:
        for line in csvfile.readlines():
            li = line.lstrip();
            if flag==1:
                sys.stdout.write(li);
                #print li;
                flag=0;
                break;
            if li.startswith(">"):
                 values=re.split(r'\t', li.rstrip('\t'));
                 checkId=isTid(values[0]);
                 if checkId==tid[num]:
                     flag=1;
                     sys.stdout.write(values[0]);
                     #print values[0];

print "finish";