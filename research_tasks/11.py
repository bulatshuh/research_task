def find_values(*args):
    list_of_values = []
    for i in range(len(args)-1):
        for element in args[0]:

            list_of_values = list(set(args[i]) & set(args[i+1]))

    return list_of_values


print(find_values([1, 4, 3], [6, 2, 8, 3], ['4', 'hi', 3, 9], [1, '4', 9]))
