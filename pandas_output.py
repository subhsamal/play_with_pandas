import pandas as pd
import sqlite3

df = pd.read_pickle('artwork.pickle')

###### Excel ########
df_xlsx = df.iloc[:50, :].copy()

# write to an single sheet excel file. install package openpyxl
df_xlsx.to_excel('artwork.xlsx', index=False)

# write to excel with multiple work sheets. Install package xlsxwriter
writer = pd.ExcelWriter('multiplesheet_artist.xlsx', engine='xlsxwriter')
df_xlsx.to_excel(writer, sheet_name='small_df', index=False)
df.to_excel(writer, sheet_name='full_df', index=False)
writer.save()


####### JSON #######
df_xlsx.to_json('artists.json', orient='table')


######### SQL: sqlite3 ########
with sqlite3.connect('my_test_db.db') as conn:
    df_xlsx.to_sql('tate', conn)

