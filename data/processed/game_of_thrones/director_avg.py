import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

director_data = pd.read_csv('D:/spark/exam/director_avg/director_avg.csv')

director_data = director_data.sort_values("avg(imdb_rating)", ascending=False)

plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(10, 8))
plt.style.use('seaborn-v0_8')

ax = sns.barplot(
    x="avg(imdb_rating)",
    y=director_data["directed_by"][::-1],
    data=director_data,
    palette="viridis",
    orient="h"
)
plt.title("Average IMDb Ratings by Director", fontsize=16, pad=20)
plt.xlabel("Average Rating", fontsize=12)
plt.ylabel("Director", fontsize=12)

plt.yticks(rotation=0, ha='right')

ax.xaxis.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()

plt.show()