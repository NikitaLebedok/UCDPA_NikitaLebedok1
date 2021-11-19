# SOURCE:  https://www.kaggle.com/nadintamer/top-spotify-tracks-of-2018

import pandas as pd
import numpy as np

data2018 = pd.read_csv('top2018.csv')

# checking for missing values in the provided dataset
miss_values = data2018.isnull().sum()
# print(miss_values)

# function to convert milliseconds into minutes
def mstohrs(millis):
    minutes = (millis / (1000 * 60)) % 60
    return minutes


# 1 - Steps I took at cleaning the data
# Removing unwanted or unclear columns
data2018.drop(['time_signature', 'valence', 'instrumentalness', 'key', 'mode', 'loudness',
               'speechiness', 'liveness', 'acousticness'], axis=1, inplace=True)

# Renaming remaining columns for better readability
data2018.rename(columns={'danceability': 'dance', 'id': 'song_id', 'name': 'song_name'}, inplace=True)

# adding new columns to see duration in minutes
data2018['duration_mins'] = data2018.duration_ms.apply(mstohrs)
#print(data2018.columns)

#Creating simple if else statement with newly converted NumPy arrays
artists = np.array(data2018['artists'])
song_length = np.array(data2018['duration_mins'].round())



# Checking if certain artist is in the list
if 'drake' in artists:
    print('drake is included in this dataset')
elif 'Drake' in artists:
    print('Perhaps Drake is added with first upper case letter ')
else:
    print('Need to check dataset for errors')


#checking the mean of all songs in the list
print('Mean lenght of the songs are ' + str(np.mean(song_length)) + ' minutes')
#checking the median lenght of all songs in the list
print('Median lenght of the songs are ' + str(np.median(song_length)) + ' minutes')




# 2 - Filtering data to explore the data in details and find new observations
# Question 1 : How many songs are above 4 minutes or 250000ms?
# Method 1 : Filtering data by using LOC method
number_of_songs = data2018.loc[data2018.duration_ms >= 250000, :]  # The answer is 8 songs
# print(number_of_songs)

# Method 2 : Filtering data by creating booleans list with 'for loop'
booleans = []  # creating list of booleans to filter against the duration of the songs and find the longest.
for duration in data2018.duration_ms:
    if duration >= 250000:

        booleans.append(True)
    else:
        booleans.append(False)

long_songs = pd.Series(booleans)  # converting boolean list into panda series
# print(data2018[long_songs]) # passing through the series list filter on the rows | #The answer is 8 songs



# Question 2 : How many times Rihanna appears in this dataset?
riri = data2018[data2018['artists'] == 'Rihanna']  # subsetting rows to find Rihanna

data2018.loc[:, 'artists']  # using loc method again

is_rihanna = data2018['artists'].isin(['Rihanna'])  # using isin method
# print(is_rihanna)
# Answer to Q2 : Rihanna is not in this dataset




# Question 3 : What are average song durations of Drake, Post Malone & Ariana Grande
unique_artists = pd.unique(data2018['artists'])  # finding all unique names

# print(unique_artists)

drake_avg = data2018[data2018['artists'] == 'Drake']['duration_mins'].mean()
postm_avg = data2018[data2018['artists'] == 'Post Malone']['duration_mins'].mean()
arianag_avg = data2018[data2018['artists'] == 'Ariana Grande']['duration_mins'].mean()
#print([drake_avg, postm_avg, arianag_avg])
# Answer on Q3: Average duration Drake - 3.61, Post Malone - 3.73, Ariana Grande - 3.36 minutes



# Question 4 : Who has more entries in the current dataset?
print(data2018['artists'].value_counts(sort=True))
# Answer on Q4: Post Malone and XXXTENTACION both has 6 entries in the current dataset.







