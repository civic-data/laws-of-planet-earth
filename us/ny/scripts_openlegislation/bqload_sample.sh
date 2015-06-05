#!
bq --project YOUR-PROJECT-HERE load --skip_leading_rows 1 nys.bills $1  date:timestamp,oid:string,otype:string,gmtime:string,data:string,senateBillNo:string,uniBill:string,law:string,sponsor:string,active:string,votes:string
# bq --project YOUR-PROJECT-HERE load --skip_leading_rows 1 nys.bills_actions $1  date:timestamp,oid:string,otype:string,gmtime:string,data:string,senateBillNo:string,uniBill:string,law:string,sponsor:string,active:string,votes:string,date2:timestamp,text2:string

