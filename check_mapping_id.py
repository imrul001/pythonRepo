#!/usr/bin/python
#Author : Hasan

import csv
import re

#                                              #        
# Method to extract mapping id from subject id #
#                                              #        
def getMapping_id(sub_id):
    result=[i for i in sub_id.split('|') if re.match('^\d+$', i)][0];
    return result;


# Method to calculate file lenght
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


# Method to search Mapid if a file
def search_id(file_name, id):
    flag=0;
    with open(file_name, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        for row in reader:
            if row[0] ==  id:
                des=row[1]
                flag=1;
                break;
            else:
                des='';
                flag=0;
                continue;
    if flag == 1:
        return des;
    else:
        return None;

length=file_len("20150128_c01_Trinity_BLASTN_UNIQ.fasta.NT.C1.Criteria.out");
tid=range(length);
with open('20150128_c01_Trinity_BLASTN_UNIQ.fasta.NT.C1.Criteria.out', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    print '#query_id'+'\t'+'Mapping_Id'+'\t'+'Description';
    for row in reader:
        tid=row[0];
        subid=row[1];
        mapid=getMapping_id(subid);
        idDes = search_id('gi.NT_out.uniq.lst.hdracc.t', mapid);
        if idDes is not None:
            print tid+'\t'+str(mapid)+'\t'+str(idDes);