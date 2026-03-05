import pandas as pd
import numpy as np
from faker import Faker

fake=Faker()

customers=pd.read_csv("dim_customer.csv")

rows=[]

for i in range(1000):

    rows.append({
    "Invoice_ID":i+1,
    "Customer_ID":customers.sample(1).iloc[0]["Customer_ID"],
    "Invoice_Date":fake.date_this_year(),
    "Invoice_Amount":round(np.random.uniform(500,10000),2),
    "Status":"Open"
    })

df=pd.DataFrame(rows)

df.to_csv("fact_ar_invoice.csv",index=False)

print("fact_ar_invoice generated")