## NOT MY ANSWER!!

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"
PUNCTUATION = ",.!?"


def checkio(text):
    text = text.upper()
    for c in PUNCTUATION:
        text = text.replace(c, " ")
    for c in VOWELS:
        text = text.replace(c, "v")
    for c in CONSONANTS:
        text = text.replace(c, "c")

    words = text.split(" ")

    count = 0
    for word in words:
        if len(word) > 1 and word.isalpha():
            if word.find("cc") == -1 and word.find("vv") == -1:
                count += 1

    return count

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"

# my answer below
# VOWELS = "AEIOUY"
# CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"
#
# def checkio(text):
#     import string
#     import re
#     exclude = set(string.punctuation)
#     for i in exclude:
#         text = text.replace(i, ' ').upper()
#     text = re.sub(r'\s+', ' ', text)
#     length = len(text)
#     if text[length-1] != ' ':
#         text += " "
#     count = 0
#     result = ""
#     for i in text:
#         if i in VOWELS:
#             result += "X"
#         elif i in CONSONANTS:
#             result += "O"
#         elif i.isdigit():
#             count += 0
#             result = "XX"
#         elif i == ' ':
#             if "XX" in result or "OO" in result or len(result) == 1 or len(result) == 0:
#                 count += 0
#                 result = ""
#             else:
#                 count += 1
#                 result = ""
#     return count







