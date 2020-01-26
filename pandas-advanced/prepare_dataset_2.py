import pandas as pd
import os


##### Prepare the score.csv file #########################
scoring = pd.read_csv(os.path.join("materials", "data", "Scoring.csv"))
# mem_mib(scoring)
# Keep a copy
scoring_orig = scoring.copy()


def recent_nhl_only(df):
    return df[(df["lgID"] == "NHL") & (df["year"] >= 1980)]


scoring = recent_nhl_only(scoring)
print(scoring.shape)

# keep columns those don't begin with the mentioned prefixes
print(scoring.columns)
scoring = scoring.filter(regex="^(?!(Post|PP|SH)).*")
print(scoring.columns)
scoring = scoring.iloc[:, [0, 1, 3, 6, 7, 8, 9, 14]]
print(scoring.columns)

# reset the index and drop the old one
scoring = scoring.reset_index(drop=True)
# alternatively, scoring.reset_index(drop = True, inplace=True)
print(scoring.head())

# save to pickle
# scoring.to_pickle("Scoring.pickle")


##### Prepare Teams.csv file #########################
teams = pd.read_csv(os.path.join("materials", "data", "Teams.csv"))
print(teams.shape)
teams = recent_nhl_only(teams)
teams = teams[["year", "tmID", "name"]]
print(teams.head())

# unique values
print(teams.nunique())

# save to pickle
teams.to_pickle("Teams.pickle")


##### Prepare TeamSplits.csv file #########################
team_splits = pd.read_csv(os.path.join("materials", "data", "TeamSplits.csv"))
print(team_splits.shape)

# drop columns by position
cols_to_drop = team_splits.columns[3:11]
team_splits = team_splits.drop(columns=cols_to_drop)
team_splits = team_splits.drop(columns="lgID")
print(team_splits.columns)

# save to pickle
team_splits.to_pickle("Team_splits.pickle")
