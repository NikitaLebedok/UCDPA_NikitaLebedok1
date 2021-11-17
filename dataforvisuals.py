import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#reading CSV file
songs50 = pd.read_csv('top50.csv', encoding=('ISO-8859-1')) # TOP 50 SONGS in 2019

#removing unwanted column
songs50.drop(['Unnamed: 0'], axis=1, inplace=True)

#cleaner column names
songs50.rename(columns={'Track.Name': 'Track_name', 'Artist.Name': 'Artist', 'Beats.Per.Minute': 'BPM'
                         , 'Loudness..dB..': 'Loudness(dB)', 'Valence.': 'Valence'
                         , 'Length.': 'Length', 'Acousticness..': 'Acousticness', 'Speechiness.': 'Speechiness'}, inplace=True)

print(songs50.columns)

# 1st VISUAL Popularity levels of top 10 artists in 2019

#art_pop = songs50.groupby('Artist.Name').sum().sort_values('Popularity', ascending=False)
#art_pop = songs50.reset_index()
#print(art_pop)

#plt.figure(figsize=(15, 5))
#plt.title('Popularity of Top 10 Artists')
#sns.barplot(x="Artist.Name", y="Popularity", data=songs50.head(10))
#plt.show()

# 2nd VISUAL
# figure size
#plt.figure(figsize=(15,8))

# Simple scatterplot
#ax = sns.barplot(x='Energy', y='Genre', data=songs50.head(10))

#ax.set_title('Scatterplot of energy per genre')
#plt.show()

# 3rd VISUAL

#figure size
#plt.figure(figsize=(15,5))

# BARPLOT to show how valence levels varies between artists
ax = sns.barplot(x='Artist', y='Valence', data=songs50.head(10), ci=None)
ax.set_title('Highest BMP per Genre', y=1.05)
ax.set(xlabel='Name of the Artist', ylabel='Valence level')
plt.xticks(rotation=90)
plt.show()

print(type(ax))
#4th Visual
#sns.set_style('whitegrid')
#sns.set_context('paper')
#sns.catplot(x='Popularity', y='Track_name', data=songs50.head(10).sort_values('Popularity', ascending=False), kind='bar')
#plt.show()


#print(songs50.head(10).sort_values('Popularity', ascending=False))