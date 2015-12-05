import requests

url = 'http://www.practicepython.org/assets/happynumbers.txt'
url2 = 'http://www.practicepython.org/assets/primenumbers.txt'

r = requests.get(url)
r2 = requests.get(url2)

text2 = r2.text.split()
common = []

for num in r.text.split():
    if num in text2:
        common.append(num)
print(common)