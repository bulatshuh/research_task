def mediana(list_of_numbers):
    median = 0
    length = len(list_of_numbers)
    sorted_list = sorted(list_of_numbers)
    if length % 2 == 0:
        median = (sorted_list[length//2] + sorted_list[length//2 - 1]) / 2
        return median
    else:
        median = sorted_list[length//2]
        return median


print(mediana([1, 2, 4, 4, 5, 6, 10, 11]))
