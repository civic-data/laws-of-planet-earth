#!/usr/bin/env python
import sys
import json
import time

jsonstring=json.load(sys.stdin)

#print jsonstring
# print len(jsonstring['response']['results'])
for dict1 in jsonstring['response']['results']:
    #print type(dict1)
    print "====",dict1['oid']
    #print "====",dict1['data']['action']['date']
    print "====",dict1['otype']
    if dict1['otype'] == 'bill':
        print "actions",len(dict1['data']['bill']['actions'])
        #pass
    elif dict1['otype'] == 'action':
        print time.strftime("%x %X",time.gmtime(float(dict1['data']['action']['date'])/1000))
    else:
        print '@@@@@@@@@@@@@other', dict1['otype']
    #print "====",dict1['data']
    for item in dict1:
        print "ITEM:", item, str(dict1[item])[0:50]

"""
for key in jsonstring:
    print key, len(jsonstring[key])
    print key, str(jsonstring[key])[0:80]
"""
