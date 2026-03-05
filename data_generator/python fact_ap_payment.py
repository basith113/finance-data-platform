import pandas as pd
import numpy as np
from faker import Faker

fake=Faker()

invoices=pd.read_csv("fact_ap_invoice.csv")

rows=[]

for i in range(800):

    inv=invoices.sample(1).iloc[0]

    rows.append({
    "Payment_ID":i+1,
    "Invoice_ID":inv["Invoice_ID"],
    "Vendor_ID":inv["Vendor_ID"],
    "Payment_Date":fake.date_this_year(),
    "Payment_Amount":round(np.random.uniform(100,inv["Invoice_Amount"]),2)
    })

df=pd.DataFrame(rows)

df.to_csv("fact_ap_payment.csv",index=False)

print("fact_ap_payment generated")