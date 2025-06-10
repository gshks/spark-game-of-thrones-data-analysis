
import matplotlib.pyplot as plt
import pandas as pd

director_count = pd.read_csv('D:/spark/exam/director_count/director_count.csv')
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['font.sans-serif'] = ['SimHei']

plt.figure(figsize=(10,10))
plt.pie(director_count['count'], labels=director_count['directed_by'], autopct='%1.1f%%')
plt.title("各导演执导剧集占比")
plt.show()