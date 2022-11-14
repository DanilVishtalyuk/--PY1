import random


def get_unique_list_numbers(min_=-10, max_=10, len_=15) -> list[int]:
    list_unique = []
    while len(list_unique) != len_:
        value = random.randint(min_, max_)
        if value not in list_unique:
            list_unique.append(value)
    return list_unique


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
