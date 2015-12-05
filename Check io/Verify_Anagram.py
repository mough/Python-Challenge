def verify_anagrams(first_word, second_word):
    import string
    exclude = set(string.punctuation)

    first_word = first_word.replace(" ", "")
    second_word = second_word.replace(" ", "")

    first_word = ''.join(ch for ch in first_word.lower() if ch not in exclude)
    second_word = ''.join(ch for ch in second_word.lower() if ch not in exclude)

    return all(first_word.count(c) == second_word.count(c) for c in first_word)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"

#  top answer:
#  return sorted(a.lower().replace(' ','')) == sorted(b.lower().replace(' ',''))