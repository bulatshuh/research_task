def is_prime_number(number: int):
    count = 0
    if number % 1 == 0 and number % number == 0:
        for i in range(2, number):
            if number % i == 0:
                count += 1

    if count == 0:
        return True
    else:
        return False


print(is_prime_number(99))
