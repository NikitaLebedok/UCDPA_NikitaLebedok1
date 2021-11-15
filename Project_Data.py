import pandas as pd

sleep_df = pd.read_csv('sleepDay_merged.csv')
weight_df = pd.read_csv('weightLogInfo_merged.csv')
active_df = pd.read_csv('dailyActivity_merged.csv')

#print(sleep_df.columns) # 'Id', 'TotalMinutesAsleep', 'SleepDay'
#print(weight_df.columns) # 'Id', 'Date', 'WeightKg', 'BMI',
#print(active_df.columns) # 'Id', 'ActivityDate', 'TotalSteps', 'TotalDistance', 'TrackerDistance', 'VeryActiveDistance'
#'ModeratelyActiveDistance', 'LightActiveDistance','Calories'

# Pulling out required information
sleep_need = sleep_df[['Id','TotalMinutesAsleep', 'SleepDay']]
weight_need = weight_df[['Id', 'Date', 'WeightKg', 'BMI']]
active_need = active_df[['Id', 'ActivityDate', 'TrackerDistance', 'VeryActiveDistance', 'ModeratelyActiveDistance', 'LightActiveDistance','Calories']]
# Merging tables together for further manipulation
sw_merge = sleep_need.merge(weight_need, on='Id')
swa_merge = sw_merge.merge(active_need, on='Id')

# print(swa_merge.isnull().values.any()) --> checking if there are any missing values in the dataframe - None
# print(swa_merge.isnull().sum()) --> to count if there are any missing values in the dataframe. Answer is 0 - no missing values

#filtering rows where single person sleeps equal to or less than 300 minutes (5hours) - Asnwer 2293 (Ids)
less_5hrs = swa_merge[swa_merge['TotalMinutesAsleep'] <= 300]
#filtering rows where single person sleeps equal to or more than 300 minutes (5hours) - Asnwer 31409 (IdS)
more_5hrs = swa_merge[swa_merge['TotalMinutesAsleep'] >= 300]

over_time = swa_merge.loc[:,['Id','Date','TotalMinutesAsleep','Calories']] # ID Progression over time to show calories burn and sleep health


participants = pd.unique(swa_merge['Id']) # Checking the number of participants this data has been collected on
print(active_df["ActivityDate"].min())
print(active_df["ActivityDate"].max())




#print(swa_merge.columns)

