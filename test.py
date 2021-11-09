import pandas as pd
import matplotlib.pyplot as plt


train_df = pd.read_csv('train_cs.csv')
test_df = pd.read_csv('test_cs.csv')
validate_df = pd.read_csv('validate_cs.csv')

a = train_df.groupby('type_attack').count()
b = a.loc[:,'duration']
c = list(b.index)
d = list(b.values)
fig, ax = plt.subplots()
ax.barh(c,d)
plt.ylabel('Type attck')
plt.xlabel('Count')
plt.title('Диаграмма распределения типов атаки')
plt.show()