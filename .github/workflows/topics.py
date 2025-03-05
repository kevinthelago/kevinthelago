import os
import requests

ROOT_DIR = os.getcwd()
print(f"Root Directory: {ROOT_DIR}")
README = ROOT_DIR + "/readme.md"


with open(README, w) as readme:
    readme.write("test write")

if __name__ == '__main__':
    print("requests test")
