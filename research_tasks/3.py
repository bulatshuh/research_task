def count_numbers(number):
    sum = 0
    if number < 0:
        number = number * -1
    for element in str(number):
        sum += int(element)
    return sum


print(count_numbers(100000021))
