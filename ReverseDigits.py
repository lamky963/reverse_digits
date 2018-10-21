def number_to_list(n):
    lst = []

    while n != 0:
        lst.insert(0, n % 10)
        n = n // 10

    return lst


def list_to_number(lst):
    num = 0
    length = len(lst)
    index = 0

    while index < length:
        num *= 10
        num += lst[index]
        index += 1

    return num


def reverse_list(lst):
    length = len(lst)
    mid = length // 2
    index = 0

    while index < mid:
        temp = lst[length-index-1]
        lst[length - index - 1] = lst[index]
        lst[index] = temp
        index += 1

    return lst


def reverse_digits(n):
    rev = list_to_number(reverse_list(number_to_list(n)))
    return rev


def digit_degree(n):
    d = 0

    while n > 10:
        sum = 0

        while n != 0:
            sum += n % 10
            n = n // 10


        n = sum
        d += 1

    return d

