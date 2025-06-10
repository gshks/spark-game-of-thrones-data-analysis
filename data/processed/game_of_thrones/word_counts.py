from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

word_counts = pd.read_csv('D:/spark/exam/word_counts/word_counts.csv')

word_freq = dict(zip(word_counts['word'], word_counts['count']))

wc = WordCloud(width=1000, height=700, background_color='white', max_words=100)
wc.generate_from_frequencies(word_freq)

plt.figure(figsize=(15, 10))
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()