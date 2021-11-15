import pandas as pd

swa_merge = pd.read_csv('swe_name.csv', index_col=0)

#checking if there are any missing values in the dataframe - None
no_values = swa_merge.isnull().sum()
# print(swa_merge.isnull().sum()) --> to count if there are any missing values in the dataframe. Answer is 0 - no missing values

#filtering rows where single person sleeps equal to or less than 300 minutes (5hours) - Asnwer 2293 (Ids)
less_5hrs = swa_merge[swa_merge['TotalMinutesAsleep'] <= 300]

#filtering rows where single person sleeps equal to or more than 300 minutes (5hours) - Asnwer 31409 (IdS)
more_5hrs = swa_merge[swa_merge['TotalMinutesAsleep'] >= 300]

# removing timestamp from column 'Date'
swa_merge['Date'] = pd.to_datetime(swa_merge['Date']).dt.date

# ID Progression over time to show calories burn and sleep health
over_time = swa_merge.loc[:,['Id','Date','TotalMinutesAsleep','Calories']]

participants = pd.unique(swa_merge['Id']) # Checking the number of participants this data has been collected on
#print(active_df["ActivityDate"].min())
#print(active_df["ActivityDate"].max())

#print(swa_merge.loc[:,['Id','Date']])
#calories_mean_of_6 = swa_merge.groupby('Id').mean() # checking mean of all columns grouped by IDs

updt_swa = swa_merge.loc[(swa_merge == 0).any(axis=1)]
print(updt_swa.shape)







