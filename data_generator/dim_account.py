import pandas as pd

accounts = [
("1000","Cash","Asset"),
("1100","Accounts Receivable","Asset"),
("1200","Inventory","Asset"),
("2000","Accounts Payable","Liability"),
("2100","Loans Payable","Liability"),
("3000","Capital","Equity"),
("4000","Sales Revenue","Revenue"),
("4100","Service Revenue","Revenue"),
("5000","Salary Expense","Expense"),
("5100","Rent Expense","Expense"),
("5200","Utilities Expense","Expense")
]

df = pd.DataFrame(accounts, columns=[
"Account_Number",
"Account_Name",
"Account_Type"
])

df["Account_ID"] = range(1,len(df)+1)

df.to_csv("dim_account.csv",index=False)

print("dim_account generated")