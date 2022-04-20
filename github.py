from utils import insert_records, create_collection, count_records
import requests


response = requests.get('https://api.github.com/users?page={page}&pagesize=100').json()

for user in response:
    new_response = requests.get(user['url']).json()


# API info:
# Non authenticated-maximum requests: 60 per hour
# With basic authentication: 5000 per hour


# data = {
#   "login": "GoncaloCoutinho",
#   "id": 83521080,
#   "node_id": "MDQ6VXNlcjgzNTIxMDgw",
#   "avatar_url": "https://avatars.githubusercontent.com/u/83521080?v=4",
#   "gravatar_id": "",
#   "url": "https://api.github.com/users/GoncaloCoutinho",
#   "html_url": "https://github.com/GoncaloCoutinho",
#   "followers_url": "https://api.github.com/users/GoncaloCoutinho/followers",
#   "following_url": "https://api.github.com/users/GoncaloCoutinho/following{/other_user}",
#   "gists_url": "https://api.github.com/users/GoncaloCoutinho/gists{/gist_id}",
#   "starred_url": "https://api.github.com/users/GoncaloCoutinho/starred{/owner}{/repo}",
#   "subscriptions_url": "https://api.github.com/users/GoncaloCoutinho/subscriptions",
#   "organizations_url": "https://api.github.com/users/GoncaloCoutinho/orgs",
#   "repos_url": "https://api.github.com/users/GoncaloCoutinho/repos",
#   "events_url": "https://api.github.com/users/GoncaloCoutinho/events{/privacy}",
#   "received_events_url": "https://api.github.com/users/GoncaloCoutinho/received_events",
#   "type": "User",
#   "site_admin": false,
#   "name": "Gonçalo Coutinho",
#   "company": null,
#   "blog": "",
#   "location": null,
#   "email": null,
#   "hireable": null,
#   "bio": null,
#   "twitter_username": null,
#   "public_repos": 4,
#   "public_gists": 0,
#   "followers": 1,
#   "following": 1,
#   "created_at": "2021-05-01T23:44:45Z",
#   "updated_at": "2022-02-21T09:16:27Z"
# }
