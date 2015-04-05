#!/usr/bin/env python3
import sys
import json
import time
import csv

jsonstring=json.load(sys.stdin)

#print jsonstring
csvwriter = csv.writer(sys.stdout)
csvwriter.writerow(['oid','otype','date','gmtime','data'])
# print len(jsonstring['response']['results'])
for dict1 in jsonstring['response']['results']:
    #print type(dict1)
    gmtime=0
    data=''
    date=''
    oid=dict1['oid']
    #print "====",dict1['data']['action']['date']
    otype=dict1['otype']
    if dict1['otype'] == 'bill':
        #print "actions",len(dict1['data']['bill']['actions'])
        data = str(dict1['data']['bill']['actions'])
        date=time.strftime("%x %X",time.gmtime(float(dict1['data']['bill']['actions'][0]['date'])/1000))
        #pass
    elif dict1['otype'] == 'action':
        gmtime=float(dict1['data']['action']['date'])
        date=time.strftime("%x %X",time.gmtime(float(dict1['data']['action']['date'])/1000))
        data = str(dict1['data']['action'])
    elif dict1['otype'] == 'transcript':
        data = str(dict1['data']['transcript']['transcriptText'])
        date=time.strftime("%x %X",time.gmtime(float(dict1['data']['transcript']['timeStamp'])/1000))
    else:
        #print '@@@@@@@@@@@@@other', dict1['otype']
        print ('@@@@@@@@@@@@@other', dict1['otype'])
        pass
    csvwriter.writerow([oid,otype,date,gmtime,data])

    #print "====",dict1['data']
    #for item in dict1:
        #print "ITEM:", item, str(dict1[item])[0:50]

"""
for key in jsonstring:
    print key, len(jsonstring[key])
    print key, str(jsonstring[key])[0:80]
"""
