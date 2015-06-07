#!

bq --project YOUR-PROJECT-HERE load --skip_leading_rows 1 nys.bills_v3 $1  publishedDateTime:timestamp,statusType,title,member_imgName,member_fullName,budget,rules,signed,adopted,resolution

