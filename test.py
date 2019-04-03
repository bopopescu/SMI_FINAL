from DBconnection import  connection2,BankConnection
from pandas import DataFrame

status, cur, db, engine = BankConnection()


transactionID=[]
cur.execute("SELECT * FROM Bank_DB.transaction WHERE clientName=  '%s'" % ('حجاج العجمي'))

transaction_df = DataFrame(cur.fetchall())
transaction_df.columns = cur.column_names
print(transaction_df)

cur.execute("SELECT * FROM SMI_DB.SuspiciousTransaction WHERE clientID=%s " % (1966002811))

suspious_transaction = cur.fetchall()
for row in suspious_transaction:
    transactionID.append(row[15])

print(transactionID)

for index, row in transaction_df.iterrows():
    print('transactions ID', row["transactionID"])
    if (row["transactionID"] in transactionID):
        print(row["transactionID"], 'Found in database')
       # transaction_df = transaction_df[transaction_df != row["transactionID"]]
        transaction_df= transaction_df[transaction_df["transactionID"] != row["transactionID"]]


print('**************')
print(transaction_df)

