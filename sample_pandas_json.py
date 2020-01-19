import pandas as pd
import json
import os


####### pandas from_records method #######

# records = [("white chocolate mocha", "$4"),
#            ("cookie crumble frappuchino", "$6")]
#
# records_df = pd.DataFrame.from_records(records, columns=["coffe", "price"])
# print(records_df)

#### Read JSON ########

def read_json_files():
    root_dir = "/Users/sumusmac/Desktop/pandas-fundamentals/02/demos/demos/" \
                         "collection-master/artworks/a"
    keys_to_use = ['id', 'all_artists', 'title', 'medium', 'dateText', 'acquisitionYear', 'height', 'width', 'units']
    artwork = []
    for root, dirs, files in os.walk(root_dir):
        for f in files:
            if f.endswith('json'):
                record = get_record_from_json_file(os.path.join(root, f), keys_to_use)
                artwork.append(record)
            break
    df = pd.DataFrame.from_records(artwork, columns=keys_to_use, index='id')
    return df


def get_record_from_json_file(sample_json, keys_to_use):
    record = []
    with open(sample_json) as artwork_f:
        file_content = json.load(artwork_f)
    for field in keys_to_use:
        record.append(file_content[field])
    return tuple(record)


json_df = read_json_files()
print(json_df)
