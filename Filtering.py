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
active_need = active_df[['Id', 'ActivityDate', 'TotalSteps', 'TotalDistance', 'TrackerDistance', 'VeryActiveDistance', 'ModeratelyActiveDistance', 'LightActiveDistance','Calories']]
# Merging tables together for further manipulation
sw_merge = sleep_need.merge(weight_need, on='Id')
swa_merge = sw_merge.merge(active_need, on='Id')


