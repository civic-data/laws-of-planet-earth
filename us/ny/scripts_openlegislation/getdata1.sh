#!
# curl "http://open.nysenate.gov/legislation/2.0/search.json?pageSize=1000&sort=modified&sortOrder=true&term=message+of+necessity" >messageofnecessity_0_999.csv
# curl "http://open.nysenate.gov/legislation/2.0/search.json?pageSize=1000&pageIdx=2&sort=modified&sortOrder=true&term=message+of+necessity" >messageofnecessity_1000_1999.csv

curl "http://open.nysenate.gov/legislation/2.0/search.json?pageSize=10&sort=modified&sortOrder=true&term=message+of+necessity" >messageofnecessity_10.json
