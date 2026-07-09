#API workflow - GET requests, headers, and params

import requests

url = "https://api.github.com/search/repositories"

params = {
        'q': 'machine learning',    #the search query
        'sort': 'stars',            #sort by star count
        'order': 'desc',            #highest first
        'per_page': 5               #keep the demo output short

    }

headers = {
        'Accept': 'application/vnd.github+json',
        'User-Agent': 'AI-Engineer-Roadmap-Day16'
        }

response = requests.get(url, headers = headers, params = params)

print(f"Status code: {response.status_code}")
print(f"Final URL: {response.url}")


