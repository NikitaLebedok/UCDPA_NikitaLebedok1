import pandas as pd

sleep_df = pd.read_csv('sleepDay_merged.csv')
weight_df = pd.read_csv('weightLogInfo_merged.csv')
active_df = pd.read_csv('dailyActivity_merged.csv')

# Pulling out required information
sleep_need = sleep_df[['Id','TotalMinutesAsleep', 'SleepDay']]
weight_need = weight_df[['Id', 'Date', 'WeightKg', 'BMI']]
active_need = active_df[['Id', 'ActivityDate', 'TotalSteps', 'TotalDistance', 'TrackerDistance', 'VeryActiveDistance', 'ModeratelyActiveDistance', 'LightActiveDistance','Calories']]

# Merging tables together for further manipulation
sw_merge = sleep_need.merge(weight_need, on='Id')
swa_merge = sw_merge.merge(active_need, on='Id')

#swa_merge.to_csv('C:/Users/NL/Desktop/swe_name.csv') downloaded new csv file to ease the code for other tabs
updt_swa = swa_merge.loc[(swa_merge == 0).any(axis=1)] # cleaning 0 from all rows
updt_swa.to_csv('C:/Users/NL/Desktop/updt_swa.csv')
