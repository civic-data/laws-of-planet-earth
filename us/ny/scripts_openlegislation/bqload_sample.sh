#!
bq --project YOUR-PROJECT-HERE --skip_leading_rows 0 nys.bills $1  date:timestamp,oid:string,otype:string,gmtime:string,data:string,senateBillNo:string,uniBill:string,law:string,sponsor:string,active:string,votes

