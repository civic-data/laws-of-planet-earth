#!/usr/bin/env python3
import sys
import json
import time
import csv

"""
"bill" : {
"amendments" : [],
"sponsor" : {
"fullname" : "Lupardo"
},
"memo" : "",
"actClause" : "AN ACT to amend the family court act, in relation to permanency hearings for youth in foster care",
"currentCommittee" : "CHILDREN AND FAMILIES",
"senateBillNo" : "A7679-2015",
"year" : 2015,
"law" : "Amd §1089, Fam Ct Act",
"votes" : [],
"fulltext" : "\n           
"""


jsonstring=json.load(sys.stdin)

#print jsonstring
csvwriter = csv.writer(sys.stdout)
#csvwriter.writerow(['oid','otype','date','gmtime','data','senateBillNo'])
#csvwriter.writerow(['oid','otype','date','gmtime','data','senateBillNo',uniBill','law','sponsor','active','votes','sameAs'])
# print len(jsonstring['response']['results'])
for dict1 in jsonstring['response']['results']:
    #print type(dict1)
    gmtime=0
    data=''
    date=''
    oid=dict1['oid']
    #print "====",dict1['data']['action']['date']
    otype=dict1['otype']


    senateBillNo = None
    uniBill = None
    law = None
    sponsor = None
    active = None
    votes = None
    sameAs = None

    if dict1['otype'] == 'bill':
        #print "actions",len(dict1['data']['bill']['actions'])
        data = str(dict1['data']['bill']['actions'])
        try:
            senateBillNo = str(dict1['data']['bill']['senateBillNo'])
        except:
            senateBillNo = ""
        try:
            uniBill = str(dict1['data']['bill']['uniBill'])
        except:
            uniBill = ""
        try:
            law = str(dict1['data']['bill']['law'])
        except:
            law = ""
        try:
            sponsor = str(dict1['data']['bill']['sponsor'])
        except:
            sponsor = ""
        try:
            active = str(dict1['data']['bill']['active'])
        except:
            active = ""
        try:
            votes = str(dict1['data']['bill']['votes'])
        except:
            votes = ""
        try:
            sameAs = str(dict1['data']['bill']['sameAs'])
        except:
            sameAs = ""

        date=time.strftime("%x %X",time.gmtime(float(dict1['data']['bill']['actions'][0]['date'])/1000))
        csvwriter.writerow([oid,otype,date,gmtime,data,senateBillNo,uniBill,law,sponsor,active,votes,sameAs])
        #pass
    elif dict1['otype'] == 'action':
        gmtime=float(dict1['data']['action']['date'])
        date=time.strftime("%x %X",time.gmtime(float(dict1['data']['action']['date'])/1000))
        data = str(dict1['data']['action'])
        #print (dict1)
        #sys.exit(1)
        try:
            senateBillNo = str(dict1['data']['action']['bill']['senateBillNo'])
        except:
            senateBillNo = ""
        try:
            uniBill = str(dict1['data']['action']['bill']['uniBill'])
        except:
            uniBill = ""
        try:
            law = str(dict1['data']['action']['bill']['law'])
        except:
            law = ""
        try:
            sponsor = str(dict1['data']['action']['bill']['sponsor'])
        except:
            sponsor = ""
        try:
            active = str(dict1['data']['action']['bill']['active'])
        except:
            active = ""
        try:
            votes = str(dict1['data']['action']['bill']['votes'])
        except:
            votes = ""
        try:
            sameAs = str(dict1['data']['action']['bill']['sameAs'])
        except:
            sameAs = ""
        csvwriter.writerow([oid,otype,date,gmtime,data,senateBillNo,uniBill,law,sponsor,active,votes,sameAs])
    elif dict1['otype'] == 'transcript':
        data = str(dict1['data']['transcript']['transcriptText'])
        date=time.strftime("%x %X",time.gmtime(float(dict1['data']['transcript']['timeStamp'])/1000))
    else:
        #print '@@@@@@@@@@@@@other', dict1['otype']
        print ('@@@@@@@@@@@@@other', dict1['otype'])
        pass

    #print "====",dict1['data']
    #for item in dict1:
        #print "ITEM:", item, str(dict1[item])[0:50]

"""
for key in jsonstring:
    print key, len(jsonstring[key])
    print key, str(jsonstring[key])[0:80]
"""
