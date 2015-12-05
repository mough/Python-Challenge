from string import punctuation


def checkio(text, words):

    global words_changed
    words_changed = []
    next_text = find_word_matches(text, words)
    return mini_word_matches(next_text, words)


def find_word_matches(text, words):
    new_text = text
    for w1 in new_text.split():
        for w2 in words.split():
            if '<span>' in w1:
                continue
            else:
                w1_mod = ''.join([w for w in w1.lower()])
                w2_mod = w2.lower()
                if w1_mod == w2_mod:
                    new_text = new_text.replace(w1, "<span>" + w1 + "</span>")
                    words_changed.append(w1)
    return new_text


def mini_word_matches(next_text, words):
    new_next_text = next_text
    spans_changed = []
    for w1 in new_next_text.split():
        for w2 in words.split():
            if '<span>' in w1:
                continue
            elif w1 in words_changed or w2.lower() in spans_changed:
                continue
            else:
                w1_mod = ''.join([w for w in w1.lower() if w not in punctuation])
                w2_mod = w2.lower()
                if w2_mod in w1_mod:
                    len_word = len([w for w in w2 if w not in punctuation])
                    where_word = new_next_text.find(w1) + w1.lower().find(w2_mod)
                    first = new_next_text[:where_word]
                    spans = new_next_text[where_word: (where_word + len_word)]
                    last = new_next_text[(where_word + len_word):]
                    spans_changed.append(spans.lower())
                    new_next_text = first + "<span>" + spans + "</span>" + last
    return new_next_text


print(checkio("Hello World! Or LOL", "hell world or lo")) # this one doesn't work, can't figure out why


