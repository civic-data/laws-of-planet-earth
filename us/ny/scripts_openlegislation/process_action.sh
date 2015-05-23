#!
COUNTER=1
while [  $COUNTER -lt 398940 ]; do
 #echo The counter is $COUNTER
 curl "http://open.nysenate.gov/legislation/2.0/search.json?pageSize=1&pageIdx=$COUNTER&sort=modified&sortOrder=true&term=otype%3Aaction%20-otype%3Atranscript" | ./process1.py
 let COUNTER=COUNTER+1 
done
