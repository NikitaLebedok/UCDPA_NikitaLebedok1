#filtering rows where single person sleeps equal to or less than 300 minutes (5hours) - Asnwer 2293 (Ids)
less_5hrs = swa_merge[swa_merge['TotalMinutesAsleep'] <= 300]

#filtering rows where single person sleeps equal to or more than 300 minutes (5hours) - Asnwer 31409 (IdS)
more_5hrs = swa_merge[swa_merge['TotalMinutesAsleep'] >= 300]

# ID Progression over time to show calories burn and sleep health
over_time = swa_merge.loc[:,['Id','Date','TotalMinutesAsleep','Calories']]

#updt_swa = swa_merge.loc[(swa_merge != 0).any(axis=1)]
#print(updt_swa.shape)

#print(swa_merge.groupby('Id').agg(['median','mean']))