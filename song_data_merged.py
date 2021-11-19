# https://www.kaggle.com/sashankpillai/spotify-top-200-charts-20202021

import pandas as pd


#Split datafrem into 2 files, for future merge
#data20_21.to_csv('C:/Users/NL/Desktop/split_songs202021.csv')


data20_21 = pd.read_csv('spotify_dataset.csv')
updtdata20_21 = pd.read_csv('split_songs202021.csv')


data20_21.drop(['Week of Highest Charting', 'Streams', 'Weeks Charted', 'Danceability', 'Energy',
               'Loudness', 'Speechiness', 'Acousticness', 'Liveness', 'Valence', 'Chord',], axis=1,
             inplace=True)

updtdata20_21.drop(['Unnamed: 0', 'Number of Times Charted','Duration (ms)','Highest Charting Position',
                    'Artist Followers', 'Index'], axis=1, inplace=True)


#Before merge
#print(data20_21.shape) # 1556, 9
#print(updtdata20_21.shape) # 1556, 3

#After merge
songids_merged = data20_21.merge(updtdata20_21, on='Song ID', suffixes=('_O','_N')) # # 1726, 14
print(songids_merged.shape)

miss_values = songids_merged.isnull().sum()
print(miss_values)
