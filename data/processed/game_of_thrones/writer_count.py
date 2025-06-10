import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

writer_countdata = pd.read_csv('D:/spark/exam/writer_count/writer_count.csv')

writer_countdata['written_by'] = writer_countdata['written_by'].apply(
    lambda x: "David & D.B." if "David Benioff & D. B. Weiss" in x else x)

total_episodes = writer_countdata['count'].sum()
writer_countdata['percentage'] = writer_countdata['count'] / total_episodes * 100

plot_data = writer_countdata.copy()
others = plot_data[plot_data['percentage'] < 5]
if len(others) > 0:
    others_row = pd.DataFrame({
        'written_by': ['其他作者'],
        'count': [others['count'].sum()],
        'percentage': [others['percentage'].sum()]
    })
    plot_data = pd.concat([plot_data[plot_data['percentage'] >= 5], others_row])

plot_data = plot_data.sort_values('count', ascending=False)

plt.figure(figsize=(8, 8))

colors = plt.cm.Paired.colors

patches, texts, autotexts = plt.pie(
    plot_data['count'],
    labels=plot_data['written_by'],
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    pctdistance=0.85,
    textprops={'fontsize': 10}
)

plt.title('《权力的游戏》各编剧剧本占比', fontsize=14, pad=20)

for text in texts:
    text.set_size(10)
for autotext in autotexts:
    autotext.set_size(10)
    autotext.set_color('white')

plt.legend(
    loc='upper left',
    bbox_to_anchor=(1, 1),
    labels=[f"{label} ({count}集)" for label, count in zip(plot_data['written_by'], plot_data['count'])]
)

plt.axis('equal')

plt.savefig('writers_distribution_small.png', dpi=300, bbox_inches='tight')

plt.show()