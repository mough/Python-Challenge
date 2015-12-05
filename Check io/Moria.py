
def checkio(find_word):
    import string
    final_word_totals = {}
    exclude = set(string.punctuation)

    find_word = ''.join(ch for ch in find_word if ch not in exclude)
    find_word = find_word.lower()

    best_word = None
    best_score = float("-inf")

    for i, word1 in enumerate(find_word.split(' ')):
        for j, word2 in enumerate(find_word.split(' ')):
            if i == j: continue
            similarity = 0

            similarity += (len(word1) / len(word2)) * 30 if len(word1) < len(word2) else (len(word2) / len(word1)) *30

            if word1[0] == word2[0]: similarity += 10
            if word1[-1] == word2[-1]: similarity += 10
            similarity += ((len(set(word1).intersection(word2)))/(len(set(word1 + word2)))) * 50

            final_word_totals[word1] = similarity
            if similarity > best_score:
                best_score = similarity
                best_word = word1

    return best_word



checkio("friend friend fred and ted")

