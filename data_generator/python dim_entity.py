import pandas as pd
from faker import Faker

fake=Faker()

rows=[]

for i in range(1,4):

    rows.append({
    "Entity_ID":i,
    "Entity_Code":f"CMP{i}",
    "Entity_Name":fake.company(),
    "Country":fake.country()
    })

df=pd.DataFrame(rows)

df.to_csv("dim_entity.csv",index=False)

print("dim_entity generated")