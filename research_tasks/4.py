def change_char(word):
    first_letter = word[0]
    word = word.replace(first_letter, '%')
    word = first_letter + word[1:]
    return word


print(change_char('qweqqrtqqdasdqwdasdqwdqdsadqqqqqqqqqq'))
