import pandas as pd
import numpy as np
from faker import Faker

fake=Faker()

accounts=pd.read_csv("dim_account.csv")
entities=pd.read_csv("dim_entity.csv")
cc=pd.read_csv("dim_cost_center.csv")
currency=pd.read_csv("dim_currency.csv")

rows=[]

for i in range(5000):

    acc=accounts.sample(1).iloc[0]

    debit=np.random.uniform(100,5000)

    if acc["Account_Type"] in ["Asset","Expense"]:
        credit=0
    else:
        credit=debit
        debit=0

    rows.append({
    "Journal_ID":i+1,
    "Account_ID":acc["Account_ID"],
    "Entity_ID":entities.sample(1).iloc[0]["Entity_ID"],
    "Cost_Center_ID":cc.sample(1).iloc[0]["Cost_Center_ID"],
    "Currency_ID":currency.sample(1).iloc[0]["Currency_ID"],
    "Debit_Amount":round(debit,2),
    "Credit_Amount":round(credit,2),
    "Description":fake.sentence()
    })

df=pd.DataFrame(rows)

df.to_csv("fact_gl_journal.csv",index=False)

print("fact_gl_journal generated")