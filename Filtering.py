import pandas as pd

swa_merge = pd.read_csv('swe_name.csv', index_col=0)

#checking if there are any missing values in the dataframe - None
no_values = swa_merge.isnull().sum()

#to count if there are any missing values in the dataframe. Answer is 0 - no missing values
missing_sum = swa_merge.isnull().sum()

# removing timestamp from column 'Date'
swa_merge['Date'] = pd.to_datetime(swa_merge['Date']).dt.date

# ID Progression over time to show calories burn and sleep health
over_time = swa_merge.loc[:,['Id','Date','TotalMinutesAsleep','Calories']]

participants = pd.unique(swa_merge['Id']) # Checking the number of participants this data has been collected on
#print(active_df["ActivityDate"].min())
#print(active_df["ActivityDate"].max())

# checking mean of all columns grouped by IDs
calories_mean_of_6 = swa_merge.groupby('Id').mean()
#print(calories_mean_of_6)


#changed_id_names = calories_mean_of_6[Id].replace({'1503960366': 'Mike','1927972279':'Lucas','4319703577':'Lucy','4558609924':'Brenda','5577150313':'Bart','6962181067':'Jen'}, inplace=True)
print(swa_merge)









