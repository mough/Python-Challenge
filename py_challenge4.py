
import urllib.request
start = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=25357')


def get_next_number(start):
    html = start.read()
    for item in html.split():
        if item.isdigit():
            next_item = item.decode("utf-8")
            url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s' % next_item
            response = urllib.request.urlopen(url)
            get_next_number(response)
        else:
            print(html)


get_next_number(start)

