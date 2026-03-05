import pandas as pd
from datetime import datetime,timedelta

start = datetime(2024,1,1)
end = datetime(2024,12,31)

rows=[]
i=1

while start<=end:

    rows.append({
    "Date_ID":i,
    "Date":start,
    "Year":start.year,
    "Month":start.month,
    "Day":start.day,
    "Quarter":(start.month-1)//3+1
    })

    start+=timedelta(days=1)
    i+=1

df=pd.DataFrame(rows)

df.to_csv("dim_date.csv",index=False)

print("dim_date generated")