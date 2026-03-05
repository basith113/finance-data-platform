import pandas as pd
from faker import Faker

fake=Faker()

rows=[]

for i in range(1,101):

    rows.append({
    "Customer_ID":i,
    "Customer_Name":fake.company(),
    "City":fake.city(),
    "Country":fake.country(),
    "Credit_Limit":fake.random_int(10000,100000)
    })

df=pd.DataFrame(rows)

df.to_csv("dim_customer.csv",index=False)

print("dim_customer generated")