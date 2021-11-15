#https://www.kaggle.com/sashankpillai/spotify-top-200-charts-20202021
#https://www.kaggle.com/nadintamer/top-spotify-tracks-of-2018

import pandas as pd

data2018 = pd.read_csv('top2018.csv')
data20_21 = pd.read_csv('spotify_dataset.csv')

#print(data20_21['Artist'])
print(data20_21['Song ID'])
