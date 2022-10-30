import pandas as pd

# Сброс ограничений на количество выводимых рядов
pd.set_option('display.max_rows', None)
# Сброс ограничений на число столбцов
pd.set_option('display.max_columns', None)
# Сброс ограничений на количество символов в записи
pd.set_option('display.max_colwidth', None)

df = pd.read_csv("StudentsPerformance.CSV")
# print(df.describe())
# df['score'] = (df['math score'] + df['reading score'] + df['writing score']).var()
# df['score'] = df['math score'] + df['reading score'] + df['writing score']
# df['score'] = df.loc[df['lunch'] == 'free/reduced']['math score'].mean()
# print(df.columns)
# print(df.shape)
# print(df.head())

"""
mean_writing_score = df['writing score'].mean()
print(mean_writing_score)
query = (df['writing score'] > mean_writing_score) & (df['reading score'] > 90)
print(df.loc[query].head())
"""
# step 6
"""
print(df.head())
query = (df.lunch == 'free/reduced')
print(df.loc[query].shape)
"""
# step 7
"""
# print('df.lunch.unique', df.lunch.unique(), type(df.lunch.unique()))
# # df['score'] = df['math score'] + df['reading score'] + df['writing score']
# query = (df.lunch == 'free/reduced')
# print(df.loc[query].describe())
# print()
# query = (df.lunch == 'standard')
# print(df.loc[query].describe())

print(df.groupby('lunch').aggregate({'math score':['mean', 'std'], 'reading score':['mean', 'std'], 'writing score' :['mean', 'std']}))
"""
# step 9
student_stats = pd.read_csv("StudentsPerformance.CSV")
print(student_stats[student_stats['parental level of education'].isin(["bachelor's degree", "master's degree"])])
