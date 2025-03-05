import os
import requests

ROOT_DIR = os.getcwd()
print(f"Root Directory: {ROOT_DIR}")
print(os.listdir(ROOT_DIR))
README = ROOT_DIR + "/readme.md"
print(f"README: {README}")

with open(README, 'r') as README:
    print(README)


with open(README, 'w') as readme:
    readme.write("test write")
    readme.close()

if __name__ == '__main__':
    print("requests test")
