#!/usr/bin/env python
import sys
import json
import csv
import urllib
import re

BILLMARKER = 'RETRIEVE BILL'
# clean1 = re.compile(r'.*QUERYDATA=\$\$')
clean1 = re.compile(r'.*QUERYDATA=')
# clean2 = re.compile(r'\$.*')
clean2 = re.compile(r'\&.*')
nomarkup = re.compile(r'<\/?[^>]+(>|$)')
clean3 = re.compile(r'.*%s'%BILLMARKER)
found = {}

def onlyascii(char):
    if ord(char) <= 9 or ord(char) > 127: return ''
    #elif ord(char) == 10 or ord(char) == 13: return ' '
    else: return char

csvwriter=csv.writer(sys.stdout)
# csvwriter.writerow(['title','link','description','text'])
csvwriter.writerow(['title','link','description','text'])
for line in sys.stdin:
    obj1 = json.loads(line)
    if BILLMARKER in obj1['content']:
        link = urllib.unquote(filter(onlyascii,obj1['link'].replace('\n','')))
        content = filter(onlyascii,obj1['content'].replace('\n',''))
        #contentclean = re.sub(clean3,'',re.sub(nomarkup, '' , content))
        contentclean = re.sub(nomarkup, '' , content)
        location = contentclean.find(BILLMARKER)
        if location != -1:
            contentclean=contentclean[location:].replace(BILLMARKER,'').strip()
        # csvwriter.writerow([ re.sub(clean2,'',re.sub(clean1, '', link)), link, contentclean, content])
        #csvwriter.writerow([ re.sub(clean2,'',re.sub(clean1, '', link)).strip(), '', ' '.join(contentclean.split()), ''])
        title=re.sub(clean2,'',re.sub(clean1, '', link)).strip()
        description=' '.join(contentclean.split())
        if not title in found:
            csvwriter.writerow([ title, '', description, ''])
            found[title]=True
        #print obj1['link']

# with open(fname) as f:
#     content = f.readlines()
