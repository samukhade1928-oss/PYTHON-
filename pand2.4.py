#Pandas Dataframe
import pandas as pd #pd is alias

#createing dictionary
dic = {
    "Name":["Amit","Rahul","Priya","Sneha","Vikas"],
    "Age":[21,22,20,23,21],
    "Marks":[85,78,92,67,88],
    "Department":["CSE","ECE","CSE","ME","CSE",]
}
#CREATEING pandas dataframe

df = pd.DataFrame(dic)
print(df.sort_values(by=["Age", "Marks"], ascending=[True, False]))