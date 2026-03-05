import pandas as pd
from faker import Faker

fake=Faker()

rows=[]

for i in range(1,101):

    rows.append({
    "Vendor_ID":i,
    "Vendor_Name":fake.company(),
    "City":fake.city(),
    "Country":fake.country()
    })

df=pd.DataFrame(rows)

df.to_csv("dim_vendor.csv",index=False)

print("dim_vendor generated")