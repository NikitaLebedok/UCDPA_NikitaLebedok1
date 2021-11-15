import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#Compare participants vs weight, totalsleeptime , bmi?

swa_merge = pd.read_csv('swe_name.csv', index_col=0)
swa_merge['Date'] = pd.to_datetime(swa_merge['Date']).dt.date # Removing timestamp from the date
participants = pd.unique(swa_merge['Id']) # Number of total participants the data was collected on
avg_of_6 = swa_merge.groupby('Id').mean() # checking mean of all columns grouped by IDs

fig, ax = plt.subplots()
ax.plot('participants', swa_merge['Calories'])
plt.show()