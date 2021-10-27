# 1. Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя,
# сохранить JSON-вывод в файле *.json.

import requests
import json

print("Имя пользователя:")
userName = input()
url = f"https://api.github.com/users/{userName}/repos"
headers = {"Accept": "application/vnd.github.v3+json"}  # рекоммендовано в разделе Resources in the REST API

response = requests.get(url, headers=headers)
print(f"Status code: {response.status_code}")

if response.status_code == 200:
    repositories = response.json()

    with open(f"Repositories_{userName}.json", "w") as file:
        json.dump(repositories, file)

    print(f"List of repositories of user {userName}:")

    for repos in repositories:
        print(repos["name"])




