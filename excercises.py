my_list = ['qwe', 1, 1.5, 'qwe', 2, 5, 3, True, -5, -10, 7]

new_list = []

for element in my_list:
    if type(element) is int and element > 0:
        new_list.append(element)

print(new_list)


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(my_list[1:3])

my_list.pop(0)

print(my_list)


# Создать кортеж
tuplex = (4, 6, 2, 8, 3, 1)
print(tuplex)

# Добавить элемент в конец кортежа
tuplex = tuplex + (9,)
print(tuplex)

# Добавить элементы на определенную позицию
tuplex = tuplex[:5] + (15, 20, 25) + tuplex[5:]
print(tuplex)

# Преобразовать кортеж в список,
# добавить элементы в список,
# затем преобразовать список в кортеж
listx = list(tuplex)
listx.append(30)
tuplex = tuple(listx)
print(tuplex)


setx = set('hello')
setx.discard('l')
print(setx)


listx = ['q', 'a', 'd', 'a', 'l']
listx.remove('a')
print(listx)


dictx = {'name': 'Sam', 'soname': 'Tompson', 'age': 31}
dictx.pop('name')
dictx.update({'qwer': 'zxcvb'})
print(dictx)


list1 = ['one', 'two', 'three', 'four']
list2 = [1, 2, 3, 4]
new_dict = {}

for element in list1:
    for el in list2:
        new_dict.update({element: el})
        break
    list2.pop(0)

print(new_dict)


list_of_keys = []
list_of_values = []

for element in new_dict.keys():
    list_of_keys.append(element)

for element in new_dict.values():
    list_of_values.append(element)

print(list_of_keys)
print(list(new_dict.keys()))
print(list_of_values)
print(list(new_dict.values()))

a = 5
print('success') if a > 5 else print('bad')


some_list = [1, 1, 2, 3, 1, 5]

for number in some_list:
    if number == 1:
        continue
    print(number)

some_list.insert(0, 'qwe')

print(some_list)

func = lambda a, b : a + b

print(func(4, 5))
