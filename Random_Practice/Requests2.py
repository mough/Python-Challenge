import requests
from bs4 import BeautifulSoup

# links = 'http://www.practicepython.org/assets/Training_01.txt'
# f = requests.get(links)
#
# text = f.text.split()

url = 'http://groups.csail.mit.edu/vision/SUN/'
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

iframexx = soup.find_all('iframe')
for iframe in iframexx:
    iframe_soup = BeautifulSoup(r.text, "html.parser")
    print(iframe_soup)



# with open('output.txt', 'a') as open_file:
#     for status in soup.find_all(class="index-scene-box"):
#         if status.a:
#             open_file.write(status.a.text.replace('\n', '').strip() + '\n')
#         else:
#             open_file.write(status.contents[0].replace('\n', '').strip() + '\n')