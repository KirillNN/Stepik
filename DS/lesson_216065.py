import pandas as pd

stud = pd.read_csv("StudentsPerformance.CSV")
print((stud.iloc[0:7]))
print((stud.loc[:7]))
print((stud.iloc[:7]))
print((stud.tail(7)))
print((stud.head(7)))
print((stud.loc[:6]))
