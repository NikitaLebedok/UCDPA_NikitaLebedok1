
#here we get rid of useless symbols to be able to separate genres
df.Genre=df.Genre.str.replace("[", "")
df.Genre=df.Genre.str.replace("]", "")
df.Genre=df.Genre.str.replace("'", "")
#now we devide genre strings by comma
df["Genre"] = df["Genre"].str.split(",")
#next command separates rows based on genres, so for each song that is marked with several genres,
#now we'll have multiple rows with one genre for each row
df=df.explode('Genre')

songids_merged['Genre'] = songids_merged['Genre'].replace


# KEEP IT FOR LATER
#songids_merged['Genre'] = songids_merged['Genre'].str.split(",")
songids_merged.Genre=songids_merged.Genre.str.replace("[", "")
songids_merged.Genre=songids_merged.Genre.str.replace("]", "")
songids_merged.Genre=songids_merged.Genre.str.replace("'", "")

songids_merged = songids_merged.explode('Genre')

fig = plt.figure(figsize = (10, 10))
ax = fig.subplots()
songids_merged.Genre.value_counts()[:25].plot(ax=ax, kind = "pie")
ax.set_ylabel("")
ax.set_title("Top 25 most popular genres")
plt.show()

