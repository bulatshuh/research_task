def find_numbers(listx:list):
    list_of_numbers = []
    for element in listx:
        if type(element) == int and element > 5:
            list_of_numbers.append(element)
    return list_of_numbers


print(find_numbers(['qwe', '1', 1.25, 5, 6, 2, 10.15]))
