import pandas as pd
from faker import Faker

fake=Faker()

departments=["Finance","Sales","Operations","HR","IT"]

rows=[]

for i,d in enumerate(departments,1):

    rows.append({
    "Cost_Center_ID":i,
    "Cost_Center_Code":f"CC{i:03}",
    "Cost_Center_Name":d,
    "Manager_Name":fake.name()
    })

df=pd.DataFrame(rows)

df.to_csv("dim_cost_center.csv",index=False)

print("dim_cost_center generated")