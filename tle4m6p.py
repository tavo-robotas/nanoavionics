import requests
from datetime import datetime

directory = 'https://celestrak.org/NORAD/elements/active.txt'
target = 'M6P'
response = requests.get(directory)
data = response.text
content = data.split('\n')
current_time = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
for i, line in enumerate(content):
    if target in line:
        with open(f'{target}_{current_time}.txt', "w+") as file:
            file.write(content[i+1])
            file.write(content[i+2])
            file.write('\n')
