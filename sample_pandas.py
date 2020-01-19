import pandas as pd
import numpy as np
import os
import pickle

# my_numpy_array = np.random.rand(3)
#
# # print(my_numpy_array)
#
# my_series = pd.Series(my_numpy_array)
# print(my_series)

# my_2d_array = np.random.rand(3,2)
# print(my_2d_array)
#
# my_df = pd.DataFrame(my_2d_array)
# print(my_df)


csv_path = os.path.join("/Users/sumusmac/Desktop/pandas-fundamentals/02/demos/demos", "collection-master",
                        "artwork_data.csv")
# df = pd.read_csv(csv_path, nrows=5)
# df =pd.read_csv(csv_path, nrows=5, index_col='id') # use the id column from the csv as the dataframe index

# df = pd.read_csv(csv_path, nrows=5, index_col='id', usecols=['id', 'artist'])

Cols_to_Use = ['id', 'artist', 'title', 'medium', 'year', 'acquisitionYear', 'height', 'width', 'units']
df = pd.read_csv(csv_path, usecols=Cols_to_Use, index_col='id')

# save as pickle
df.to_pickle("artwork.pickle")