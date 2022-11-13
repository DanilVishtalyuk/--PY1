import random


def get_unique_list_numbers() -> list[int]:
    list_unique = []
    while len(list_unique) != 15:
        value = random.randint(-10, 10)
        if value not in list_unique:
            list_unique.append(value)
    return list_unique


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))


