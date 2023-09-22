def count_letters(slovo, letter):
    count = 0
    slovo_list = list(slovo)
    count = slovo_list.count(letter)
    return count


print(count_letters('wildberries', 's'))
