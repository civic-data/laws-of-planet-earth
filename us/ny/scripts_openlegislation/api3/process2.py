#!/usr/bin/env python3
import sys
import json
import csv
from datetime import datetime

# url -X PUT -d '{"highestScore":3}' 'https://nysenate.firebaseio.com/leaderboard.json'

objectin = json.load(sys.stdin)
csvwriter = csv.writer(sys.stdout)
MISSING_participantsCount=-1

csvwriter.writerow ( ['publishedDateTime','statusType','title','member_imgName','member_fullName','budget','rules'])
for item in objectin:
    # print (type(item), len(item))
    for item2 in item:
        # print (type(item2), len(item2))
        # print (item2)
        try:
# image is here: http://openleg-dev.nysenate.gov/static/img/business_assets/members/mini/413_john_j._bonacic.jpg
            # print ( item2['result']['publishedDateTime'], item2['result']['status'], item2['result']['title'],item2['result']['sponsor']['member']['imgName'])
            csvwriter.writerow ( [item2['result']['publishedDateTime'], item2['result']['status']['statusType'], item2['result']['title'],item2['result']['sponsor']['member']['imgName'],item2['result']['sponsor']['member']['fullName'],item2['result']['sponsor']['rules'], item2['result']['sponsor']['budget']])

            # print (item2['result']['status']['statusType'])
        except Exception as e:
            try:
                csvwriter.writerow ( [item2['result']['publishedDateTime'], item2['result']['status']['statusType'], item2['result']['title'],item2['result']['sponsor']['member'],'',item2['result']['sponsor']['rules'], item2['result']['sponsor']['budget']])
            except Exception as e:
                print (e,'qqq:',item2,file=sys.stderr)

        #sys.exit(1)
#   {
#       'highlights': {},
#       'rank': 1,
#       'result': {
#           'activeVersion': '',
#           'session': 2015,
#           'programInfo': None,
#           'basePrintNo': 'J2697',
#           'vetoed': False,
#           'title': "Honoring Monsignor John McCann upon the occasion of his retirement as Pastor of St. Mary's Church in Manhasset, New York",
#           'substitutedBy': None,
#           'summary': '',
#           'billType': {
#               'resolution': True,
#               'chamber': 'SENATE',
#               'desc': 'Regular and Joint'
#           },
#           'sponsor': {
#               'member': {
#                   'memberId': 397,
#                   'shortName': 'MARTINS',
#                   'districtCode': 7,
#                   'imgName': '397_jack_m._martins.jpg',
#                   'fullName': 'Jack M. Martins',
#                   'chamber': 'SENATE',
#                   'sessionYear': 2015
#               },
#               'budget': False,
#               'rules': False
#           },
#           'publishedDateTime': '2015-06-05T09:16:05',
#           'milestones': {
#               'items': [],
#               'size': 0
#           },
#           'printNo': 'J2697',
#           'adopted': False,
#           'signed': False,
#           'year': 2015,
#           'status': {
#               'statusDesc': 'In Senate Committee',
#               'committeeName': 'Finance',
#               'statusType': 'IN_SENATE_COMM',
#               'actionDate': '2015-06-05',
#               'billCalNo': None
#           }
#       }
#   }
# egrep "printNo|publishedDateTime|imgName|title" *FOR*
