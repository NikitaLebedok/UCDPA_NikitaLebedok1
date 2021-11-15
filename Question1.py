import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Compare participants vs weight, totalsleeptime , bmi?

sleep_df = pd.read_csv('sleepDay_merged.csv')
weight_df = pd.read_csv('weightLogInfo_merged.csv')
active_df = pd.read_csv('dailyActivity_merged.csv')

# Pulling out required information
sleep_need = sleep_df[['Id','TotalMinutesAsleep', 'SleepDay']]
weight_need = weight_df[['Id', 'Date', 'WeightKg', 'BMI']]
active_need = active_df[['Id', 'ActivityDate', 'TrackerDistance', 'VeryActiveDistance', 'ModeratelyActiveDistance', 'LightActiveDistance','Calories']]
# Merging tables together for further manipulation
sw_merge = sleep_need.merge(weight_need, on='Id')
swa_merge = sw_merge.merge(active_need, on='Id')

participants = pd.unique(swa_merge['Id']) # Number of total participants the data was collected on
avg_of_6 = swa_merge.groupby('Id').mean() # checking mean of all columns grouped by IDs
print(avg_of_6)


sns.relplot(x="participants", y="Calories", data=swa_merge, kind="line")
plt.show()