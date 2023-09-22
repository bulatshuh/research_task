def find_numbers():
    list_of_numbers = []
    for i in range(1500, 2701):
        if i % 5 == 0 and i % 7 == 0:
            list_of_numbers.append(i)

    return list_of_numbers


print(find_numbers())
