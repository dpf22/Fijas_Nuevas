import requests

url = "https://www.thesportsdb.com/api/v1/json/YOUR_API_KEY/searchteams.php?t=Barcelona"
response = requests.get(url)
data = response.json()
print(data)
