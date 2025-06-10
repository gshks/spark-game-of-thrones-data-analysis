import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.sans-serif'] = ['SimHei'] 
plt.rcParams['axes.unicode_minus'] = False
writer_avg = pd.read_csv('D:/spark/exam/writer_avg/writer_avg.csv')

writer_avg['written_by'] = writer_avg['written_by'].apply(
    lambda x: "David & D.B." if "David Benioff & D. B. Weiss" in x else x)

plt.figure(figsize=(10, 10))

barplot = sns.barplot(
    y='written_by',
    x='avg_imdb_rating',
    data=writer_avg,
    palette='viridis'
)

plt.title('《权力的游戏》不同编剧的平均IMDb评分', fontsize=14, pad=20)  # 调整标题字体大小
plt.xlabel('平均IMDb评分', fontsize=10)
plt.ylabel('编剧', fontsize=10)

plt.yticks(rotation=0, ha='right')

for p in barplot.patches:
    barplot.annotate(
        format(p.get_width(), '.2f'),
        (p.get_width(), p.get_y() + p.get_height() / 2.),
        ha='left', va='center',
        xytext=(10, 0),
        textcoords='offset points',
        fontsize=8
    )
plt.tight_layout()

plt.savefig('writers_ratings_horizontal.png', dpi=300, bbox_inches='tight')

plt.show()