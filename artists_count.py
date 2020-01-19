import pandas as pd

#### count the number of unique artists #####
def unique_artist_count(df):
    artists = df['all_artists']
    unique_artists_df = pd.unique(artists)
    return len(unique_artists_df)


df = pd.read_pickle("dataframe.pickle")
print(f"Number of unique artists: {unique_artist_count(df)}")

##### occurrence count for George Jones #####
s = df['all_artists'] == "George Jones"  # output is a pandas series of True/False
print(f"Occurrence of George Jones: {s.value_counts()[True]}")


##### pandas loc vs iloc #####
# loc uses row index and column name to filter elements
# eg: Find the artist at row index 2849 and column 'all_artists'. Which is David Cox

print(f"Artist is: {df.loc[2849, 'all_artists']}")

# iloc uses position of rows and columns. Count starts from o.
print(f"Artist at first row and first column of the df: {df.iloc[0,0]}")

# Calculate area
df.loc[:, 'width'] = pd.to_numeric(df['width'], errors='coerce')
df.loc[:, 'height'] = pd.to_numeric(df['height'], errors='coerce')

# create a new area column
df['area'] = df['height'] * df['width']
df.to_pickle("df_with_area.pickle")