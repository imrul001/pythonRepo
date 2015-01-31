#!/usr/bin/python
#Author : Hasan

import csv
import re

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def search_id(file_name,id):
    length=file_len(file_name);
    for num in range(0,length):
        with open(file_name, 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter='\t')
            for row in reader:
                if row[0] ==  id:
                    return True;
                else:
                    return False;

def search_in_blast(blast_result_file_name,id):
    length=file_len(blast_result_file_name);
    for num in range(0,length):
        with open(blast_result_file_name, 'rb') as csvfile:
            for line in csvfile.readlines():
                li = line.lstrip()
                if not li.startswith("#"):
                    values=re.split(r'\t', li.rstrip('\t'));
                    if id ==  values[0]:
                        return True;
                    else:
                        return False;

def getResult(result):
    if result == True:
        return 1
    else:
        return 0

def getResultFromBlast(result):
    if result == True:
        return 'y';
    else:
        return 'n';

length=file_len("20150128_c01_Trinity_BLASTN_UNIQ.fasta.lngth");
tid=range(length);
with open('20150128_c01_Trinity_BLASTN_UNIQ.fasta.lngth', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    print '#query_id'+'\t'+'wssvout'+'\t'+'ntout'+'\t'+'wssvBlastout'+'\t'+'ntBlastout';
    for row in reader:
        tid=row[0];
        idFoundWSSVout = search_id('20150128_c01_Trinity_BLASTN_UNIQ.fasta.WSSV.C1.Criteria.out',tid);
        idFoundNTVout = search_id('20150128_c01_Trinity_BLASTN_UNIQ.fasta.NT.C1.Criteria.out',tid);
        SubjectFoundINwssv = getResultFromBlast(search_in_blast('20150128_c01_Trinity_BLASTN_UNIQ.fasta.WSSV.out',tid));
        SubjectFoundINnt = getResultFromBlast(search_in_blast('20150128_c01_Trinity_BLASTN_UNIQ.fasta.NT.out',tid));
        wssvout=getResult(idFoundWSSVout);
        ntout=getResult(idFoundNTVout);
        blastwssvout=getResultFromBlast(SubjectFoundINwssv);
        blastntout=getResultFromBlast(SubjectFoundINnt);
        print tid+'\t'+str(wssvout)+'\t'+str(ntout)+'\t'+SubjectFoundINwssv+'\t'+SubjectFoundINnt;

