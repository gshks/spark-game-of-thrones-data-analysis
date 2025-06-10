import pandas as pd

episodes_data = pd.read_csv('./数据集/game_of_thrones.csv')
imdb_data = pd.read_csv('./数据集/game_of_thrones_imdb.csv')

episodes_data['original_air_date'] = pd.to_datetime(episodes_data['original_air_date'], errors='coerce')
imdb_data['original_air_date'] = pd.to_datetime(imdb_data['original_air_date'], format='%d %b %Y', errors='coerce')

imdb_data = imdb_data[['title', 'original_air_date', 'imdb_rating', 'total_votes']]
total_data = episodes_data.merge(imdb_data, how='left', on=['title', 'original_air_date'])

total_data.to_csv('./数据集/game_of_thrones_sum.csv', encoding='utf-8')