## https://stackoverflow.com/questions/17301938/making-a-request-to-a-restful-api-using-python
## https://habr.com/ru/companies/macloud/articles/562700/

## https://geek-jokes.sameerkumar.website/api?format=json:

import requests
url = 'https://geek-jokes.sameerkumar.website/api?format=json:'

response = requests.get(url)

print(response.json())