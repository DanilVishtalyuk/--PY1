def get_count_char(str_):
    letter_dict = {}
    str_ = str_.lower()
    list_str = str_.split()
    str_with_separate = "".join(list_str)
    for letter in str_with_separate:
        if letter in letter_dict:
            letter_dict[letter] += 1
        elif letter.isalpha():
            letter_dict[letter] = 1

    return letter_dict


def get_percent_char(dict_=None):
    if dict_ is None:
        dict_ = {}

    new_letter_dict = {}
    total_letter = sum(dict_.values())

    for letter in dict_:
        new_letter_dict[letter] = round((dict_.get(letter) / total_letter) * 100, 2)
    return new_letter_dict

# TODO посчитать количество каждой буквы в строке в аргументе str_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str))
#новый словарь, процентное отношение символов округленно до 2 знаков после запятой
print(get_percent_char(get_count_char(main_str)))
