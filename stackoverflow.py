from utils import insert_records, create_collection, count_records
import requests
import requests_cache
import time
import re
from IPython.display import clear_output


def fetching_data(page: int):
    '''Fetches user data from the stackexchange API'''
    users_url = f'https://api.stackexchange.com/2.3/users?page={page}&pagesize=100&order=desc&sort=modified&site=stackoverflow&filter=!56ApJn82ELRG*IWQxo6.gXu9qS90qXxNmY8e9b'
    response = requests.get(users_url)
    return response


# Create Cache
requests_cache.install_cache(cache_name='stackoverflow_cache', backend='sqlite', expire_after=6000)

# Create Collection
stackoverflow = create_collection("Stackoverflow")

# Initialize list to save records
results = []

# Fetch data until the page 25 (API limit without key)
for i in range(1, 26):
    # Print status
    print(f"Requesting page {i}/{25}")

    # Get Data
    response = fetching_data(i)
    result = response.json()

    # Save the users
    for user in result['items']:
        user['_id'] = user.pop('user_id')
        email_name = re.sub('[^a-zA-Z0-9 \n\.]', '', user['display_name'])
        user['email'] = 'bigdataprogrammingteam1+'+email_name.replace(' ', '')+'@gmail.com'
        results.append(user)

    # Print if results came from cache or not
    now = time.ctime(int(time.time()))
    using_cache = response.from_cache
    print(f'Time: {now} / Used Cache: {using_cache}')
    clear_output(wait=True)

    # If the result is not in cache sleep to avoid throttling
    if result['has_more']:
        if not using_cache:
            time.sleep(11)
    else:
        break


# Insert records into MongoDB
before = count_records(stackoverflow)
insert_records(results, stackoverflow)
after = count_records(stackoverflow)
print(f"There are a total of {after-before} new records in mongoDB")
