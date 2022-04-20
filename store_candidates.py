from preprocessing import df
from utils import create_collection, insert_records, delete_records
import ast

# Create the collection to store the selected candidates
selected_candidates = create_collection('Selected_candidates')

# Delete former candidates from mongodb
delete_records(query={"_id": {"$gte": 0}}, collection=selected_candidates)

# Create a list with the new candidates
selected_df = df.loc[df['Selected'] == True][['display_name', 'email']]
candidates_list = []
candidate_id = 1
for index, row in selected_df.iterrows():
    row['_id'] = candidate_id
    file = row.to_json()
    # We have a string representation of dict, we have to convert to dict
    dict_file = ast.literal_eval(file)
    candidates_list.append(dict_file)
    candidate_id += 1

# Insert the new candidates into mongodb
insert_records(candidates_list, selected_candidates)
