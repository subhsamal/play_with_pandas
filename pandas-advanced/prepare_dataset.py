import os
import pandas as pd
from pandas import isnull


# read the master.csv file
master = pd.read_csv(os.path.join("materials", "data", "Master.csv"))
print(master.head())    # shows first 5 rows
print(master.shape)     # shows total number of rows and columns in the dataset.
print(master.columns)   # shows the columns present.

# Check the count for number of players with no playerID
w_pid, wo_pid = master["playerID"].pipe(isnull).value_counts()
print(w_pid, wo_pid)

# pandas' dropna method drops any rows with missing values for a specified column
master_orig = master.copy()
master_orig = master_orig.dropna(subset=["playerID"])
print(master_orig.shape)

# both columns should have missing values for a row to be dropped.
master_orig = master_orig.dropna(subset=["firstNHL", "lastNHL"], how="all")

# filter based on lastNHL
master_orig = master_orig.loc[master_orig["lastNHL"] >= 1980]
print(master_orig.shape)

# filter based on column names.
columns_to_keep = ["playerID", "firstName", "lastName", "pos", "birthYear", "birthMon", "birthDay",
                   "birthCountry", "birthState", "birthCity"]
print(master_orig[columns_to_keep].head())
# pandas' filter method can parse regex
master_orig = master_orig.filter(regex="(playerID|pos|^birth)|(Name$)")
# master_orig.filter(columns_to_keep).head()
print(master_orig.columns)

# set index to a column name
master_orig = master_orig.set_index("playerID")
print(master_orig.head())

# save the dataset to a pickle
master_orig.to_pickle("Master.pickle")

##########################################################
##### Prepare the score.csv file #########################

