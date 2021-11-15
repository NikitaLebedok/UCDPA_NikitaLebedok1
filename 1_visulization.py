import pandas as pd
import matplotlib.pyplot as plt

swa_merge = pd.read_csv('updt_swa.csv', index_col=0)

swa_merge.groupby(['Id']).size().plot(kind='bar')
set_xlabel = 'Id'
set_ylabel = 'Calories'
plt.show()