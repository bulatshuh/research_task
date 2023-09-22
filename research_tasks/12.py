def func(arr):
    for i in range(len(arr) - 2):
        el = arr[i:i + 3]
        if el == list(range(min(el), max(el) + 1)):
            return True
    return False


print(func([1, 2, 2, 4, 66, 6, 7, 1]))
print(func([1, 2, 2, 3, 4, 66, 6, 7, 1]))
print(func([1, 2, 3, 3, 4, 66, 6, 7, 1]))
print(func([1, 2, 2, 3, 4, 66, 6, 7, 8]))
print(func([1, 2, 2, 3, 4, 5, 6, 7, 1]))
print(func([1, 2, 2, 3, 9, 66, 6, 7, 1]))
