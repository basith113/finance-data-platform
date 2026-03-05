import pandas as pd
import numpy as np
from faker import Faker

fake=Faker()

vendors=pd.read_csv("dim_vendor.csv")

rows=[]

for i in range(1000):

    rows.append({
    "Invoice_ID":i+1,
    "Vendor_ID":vendors.sample(1).iloc[0]["Vendor_ID"],
    "Invoice_Date":fake.date_this_year(),
    "Invoice_Amount":round(np.random.uniform(500,15000),2),
    "Status":"Open"
    })

df=pd.DataFrame(rows)

df.to_csv("fact_ap_invoice.csv",index=False)

print("fact_ap_invoice generated")