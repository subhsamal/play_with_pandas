import pandas as pd

df = pd.read_pickle('dataframe.pickle')
df_subset = df.iloc[:20, :].copy()

grouped_artists = df_subset.groupby('all_artists')
print(type(grouped_artists))

# get the artists dataframe in groups
for name, group_df in grouped_artists:
    print(name)
    print(group_df)

print(df_subset)
print(df)

# pandas filter: to get rid of certain groups. Only keep the groups if artist name appears more than once.
condition = lambda x: len(x.index) > 1
dup_name_artists = grouped_artists.filter(condition)
dup_name_artists.sort_values('medium', inplace=True)
print(dup_name_artists)
