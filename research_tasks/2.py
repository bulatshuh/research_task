def is_anigram(first_word, second_word):
    if len(first_word) == len(second_word):
        word1 = list(first_word)
        word2 = list(second_word)
        for letter in word1:
            if letter in word2:
                word2.remove(letter)
            else:
                break
        if len(word2) == 0:
            return True
        else:
            return False
    else:
        return False


print(is_anigram('beluga', 'begula'))
