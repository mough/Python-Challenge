import requests
from bs4 import BeautifulSoup

url = 'https://www.imgur.com'
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

with open('output.txt', 'a') as open_file:
    for status in soup.find_all("p"):
        if status.a:
            open_file.write(status.a.text.replace('\n', '').strip() + '\n')
        else:
            open_file.write(status.contents[0].replace('\n', '').strip() + '\n')


