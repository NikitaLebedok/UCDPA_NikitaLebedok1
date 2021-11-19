import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# reading CSV file
songs50 = pd.read_csv('top50.csv', encoding=('ISO-8859-1'))  # TOP 50 SONGS in 2019

# removing unwanted column
songs50.drop(['Unnamed: 0'], axis=1, inplace=True)

# cleaner column names
songs50.rename(columns={'Track.Name': 'Track_name', 'Artist.Name': 'Artist', 'Beats.Per.Minute': 'BPM'
    , 'Loudness..dB..': 'Loudness(dB)', 'Valence.': 'Valence'
    , 'Length.': 'Length', 'Acousticness..': 'Acousticness', 'Speechiness.': 'Speechiness'},
               inplace=True)

# checking column names after renaming
print(songs50.columns)

# VISUAL #1
# figure size
#fig = plt.figure(figsize=(17,6))
# setting the background style for the barplot
#sns.set_style('whitegrid')
# setting the color paletter for the barplot
#sns.set_palette('cubehelix')
# BARPLOT Valence levels of top 10 songs in 2019
#ax = sns.barplot(x='Valence', y='Track_name', data=songs50.head(10).sort_values('Valence', ascending=False), ci=None)
#ax.set_title('Level of Valence of top 10 songs in 2019', y=1)
#ax.set(xlabel='Level of Valence', ylabel='Name of the Song')
#plt.yticks(rotation=45)
#fig.savefig("visual1.png")
#plt.show()

# VISUAL #2
# figure size
#fig2 = plt.figure(figsize=(17,6))
# setting the background style for the barplot
#sns.set_style('white')
# setting the color paletter for the barplot
#sns.set_palette('deep')
# BARPLOT Popularity of top 10 songs in 2019
#ax = sns.barplot(x='Popularity', y='Track_name', data=songs50.head(10).sort_values('Popularity', ascending=False), ci=None)
#ax.set_title('Level of Popularity of top 10 songs in 2019', y=1.05)
#ax.set(xlabel='Popularity', ylabel='Name of the Song')
#plt.yticks(rotation=45)
#fig2.savefig("visual2.png")
# plt.show()


# VISUAL #3

# setting the figure size
#fig3 = plt.figure(figsize=(8,5))
# setting the style
#sns.set_style('darkgrid')
#adding variables to the scatterplot
#ax = sns.scatterplot(x='Danceability', y='Energy', data=songs50)
# setting the title
#ax.set_title('Question: Is it easier to dance when the song is more energetic?', y=1.03)
# setting the labels on both axis
#ax.set(xlabel='How easy is it to Dance?', ylabel='Energy levels')
#fig3.savefig("visual3.png")
#displaying the plot
#plt.show()



# 4th Visual
# setting the figure size
fig4 = plt.figure(figsize=(8,5))
# setting the style
sns.set_style('white')
sns.set_palette('bright')
# adding variables to the scatterplot
ax = sns.scatterplot(x='Energy', y='Valence', data=songs50) #c=colors
# setting the title
ax.set_title('Question: Does Energy affect the positivity of the song?', y=1.03)
# setting the labels on both axis
ax.set(xlabel='Energy levels', ylabel='Valence levels')
fig4.savefig("visual4.png")
# displaying the plot
#plt.show()


# 5th VISUAL
# Catplot visualising count of all genres of top 50 songs in 2019
#sns.set(rc={'figure.figsize':(8,5)})
#sns.set_style('darkgrid')
#sns.set_palette('bright')
#g = sns.catplot(data=songs50 ,y="Genre", kind="count", edgecolor="1")
#g.set(xlabel='Count of genres of 50 top songs in 2019', ylabel='Genres of top 50 songs in 2019')
#plt.show()


