#!/usr/bin/env python3

# http://openleg-dev.nysenate.gov/api/3/bills/search?key=6E9qUekhHoo4gAyZc4God2tC6KhBHxvd&limit=1000&term=(*)

#   "success": true,
#   "message": "",
#   "responseType": "search-results list",
#   "total": 97043,
#   "offsetStart": 1,
#   "offsetEnd": 10,
#   "limit": 10,
#   "result": {
#       "items": [{
#                   "result": {
#                       "printNo": "J2697",
#                       "billType": {
#                           "chamber": "SENATE",
#                           "desc": "Regular and Joint",
#                           "resolution": true
#                       },
#                       "title": "Honoring Monsignor John McCann upon the occasion of his retirement as Pastor of St. Mary's Church in Manhasset, New York",
#                       "activeVersion": "",
#                       "year": 2015,
#                       "publishedDateTime": "2015-06-05T09:16:05",
#                       "substitutedBy": null,
#                       "sponsor": {
#                           "member": {
#                               "memberId": 397,
#                               "shortName": "MARTINS",
#                               "sessionYear": 2015,
#                               "chamber": "SENATE",
#                               "fullName": "Jack M. Martins",
#                               "districtCode": 7,
#                               "imgName": "397_jack_m._martins.jpg"
#                           },


import sys
import json
import time
import csv
import requests


now=(int(time.time()))
list1=[]
i=1
pagesize=1000

while True:
    # print (now)
    #end = now
    #now = now - (60*60*24*7*16)
    r = requests.get("http://openleg-dev.nysenate.gov/api/3/bills/search?sort=status.actionDate:DESC&key=6E9qUekhHoo4gAyZc4God2tC6KhBHxvd&limit=1000&term=(*)&offset=%s" % (i))
    # json.dump(sys.stdout,r.json())
    # print(type(r.json()))
    #print (i,len(r.json()),file=sys.stderr)

    #1575001 {'message': '', 'total': 97043, 'offsetEnd': 97043, 'success': True, 'offsetStart': 1575001, 'responseType': 'empty list', 'result': {'size': 0, 'items': []}, 'limit': 1000}

    print (i,len(r.json()['result']['items']),r.json()['total'],file=sys.stderr)
    list1 += [r.json()['result']['items']]

    if i > r.json()['total']:
        break
    i+=pagesize

    if len(r.json()) == 0:
        break
    # sys.exit(1)
print(json.dumps(list1))
