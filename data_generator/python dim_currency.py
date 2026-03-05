import pandas as pd

data=[
(1,"USD","US Dollar"),
(2,"INR","Indian Rupee"),
(3,"EUR","Euro")
]

df=pd.DataFrame(data,columns=[
"Currency_ID",
"Currency_Code",
"Currency_Name"
])

df.to_csv("dim_currency.csv",index=False)

print("dim_currency generated")