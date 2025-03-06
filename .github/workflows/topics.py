import os
import requests

WORKING_DIR = os.getcwd()
README = WORKING_DIR + "/README.md"
INTRODUCTION = WORKING_DIR + "/Introduction.md"
LANGUAGES_AND_TOOLS = WORKING_DIR + "/LanguagesAndTools.md"

with open(LANGUAGES_AND_TOOLS, 'w') as languages_and_tools:
    topics = set()
    i = 0

    while True:
        response = requests.get(f'https://api.github.com/users/kevinthelago/repos?page={i}')
        data = response.json()
        i = i + 1

        if len(data) == 0:
            break

        for repo in data:
            name = repo.get('name')
            url = repo.get('url')
            topics.update(repo.get('topics'))

    for topic in topics:
        languages_and_tools.write(
            f'<img align="left" alt="{topic}" style="width: 32px; padding-right: 8px;" src="https://skillicons.dev/icons?i={topic}" />'
        )
    languages_and_tools.close()


with open(README, 'w') as readme:
    with open(INTRODUCTION, 'r') as introduction:
        for line in introduction:
            readme.write(line)
        introduction.close()

    with open(LANGUAGES_AND_TOOLS, 'r') as languages_and_tools:
        for line in languages_and_tools:
            readme.write(line)
        languages_and_tools.close()
    readme.close()
