#!/usr/bin/python
# Author : Hasan
import csv
import re
import sys

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def check_evalue(evalue):
    if evalue <= 1e-6:
        return True;
    else:
        return False;

def check_identity(identity):
    if identity >= 70.0:
        return True;
    else:
        return False;

def check_query_length(length, qStart,qEnd):
    len = calculate_query_length(length, qStart,qEnd);
    if len >= 0.5:
        return True;
    else:
       return False;

def calculate_query_length(length, qStart,qEnd):
    len = (abs(qStart - qEnd)+1)/length;
    return str(len).strip();

length=file_len("20150128_c01_Trinity_BLASTN_UNIQ.fasta.lngth");
tid=range(length);
len=range(length);

i=0;
with open('20150128_c01_Trinity_BLASTN_UNIQ.fasta.lngth', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    for row in reader:
        tid[i]=row[0];
        len[i]=row[1];
        i=i+1;
values=range(13);

for num in range(0,length):
    with open('20150128_c01_Trinity_BLASTN_UNIQ.fasta.NT.out', 'rb') as csvfile:
        for line in csvfile.readlines():
            li = line.lstrip()
            if not li.startswith("#"):
                 values=re.split(r'\t', li.rstrip('\t'));
                 cevalue=check_evalue(float(values[10]));
                 cidentity= check_identity(float(values[2]));
                 queryl=check_query_length(float(values[3]), float(values[6]), float(values[7]));
                 query_length=calculate_query_length(float(values[3]), float(values[6]), float(values[7]));
                 if(tid[num] ==  values[0] and cevalue==True and cidentity==True and queryl==True):
                     result=range(13);
                     values.append(query_length);
                     sys.stdout.write(values[0]+'\t'+values[1]+'\t'+values[2]+'\t'+values[3]+'\t'+values[4]+'\t'+values[5]+'\t'+values[6]+'\t'+values[7]+'\t'+values[8]+'\t'+values[9]+'\t'+values[10]+'\t'+values[12]+'\t'+values[11]);
                    # wrote the query length in 12th column
