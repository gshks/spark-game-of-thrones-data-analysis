import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

season_avgdata = pd.read_csv('D:/spark/exam/season_avgdata/season_avgdata.csv')

plt.figure(figsize=(15, 10))
sns.set_style("whitegrid")

# 第一个折线图：每季平均观看人数
plt.subplot(3, 1, 1)
sns.lineplot(x="season", y="avg_us_viewers", data=season_avgdata, marker='o', color='b')
plt.title('Average US Viewers per Season (in millions)')
plt.xlabel('Season')
plt.ylabel('Viewers (millions)')
plt.xticks(range(1, 9))

# 第二个折线图：每季平均IMDb评分
plt.subplot(3, 1, 2)
sns.lineplot(x="season", y="avg_imdb_rating", data=season_avgdata, marker='o', color='g')
plt.title('Average IMDb Rating per Season')
plt.xlabel('Season')
plt.ylabel('IMDb Rating')
plt.ylim(7, 10)  # 设置y轴范围以更好显示差异
plt.xticks(range(1, 9))

# 第三个折线图：每季平均投票人数
plt.subplot(3, 1, 3)
sns.lineplot(x="season", y="avg_total_votes", data=season_avgdata, marker='o', color='r')
plt.title('Average Total Votes per Season')
plt.xlabel('Season')
plt.ylabel('Total Votes')
plt.xticks(range(1, 9))

plt.tight_layout()
plt.savefig('game_of_thrones_season_analysis.png', dpi=300)
plt.show()