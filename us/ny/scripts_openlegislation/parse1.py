#!/usr/bin/env python
import sys
import json
import csv
import time
import datetime

# map1[item3]=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime(int(item2[item3])/1000))
csvreader = csv.DictReader(sys.stdin, delimiter=',', quotechar='"')
csvwriter = csv.writer(sys.stdout, delimiter=',', quotechar='"')
headers=['oid','otype','gmtime','data','senateBillNo','uniBill','law','sponsor','active','votes']
headersout=['date']+headers
csvwriter.writerow(headersout)
for row in csvreader:
    #print row
    rowout=[]
    try: 
        date = datetime.datetime.strptime( row['date'], "%m/%d/%Y %H:%M:%S" )
    except:
        date = datetime.datetime.strptime( row['date'], "%m/%d/%y %H:%M:%S" )
    #print time.strftime('%Y-%m-%dT%H:%M:%SZ',row['date'])
    rowout+=[row['date']]
    for item in headers:
        rowout+=[row[item]]
    csvwriter.writerow(rowout)
