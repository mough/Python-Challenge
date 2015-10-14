
import urllib.request
import pickle
text = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/banner.p')

y = pickle.load(text)

lines = []
for row in y:
    line = []
    for c, num in row:
        line.append(c * num)
    lines.append("".join(line))

print("\n".join(lines))

