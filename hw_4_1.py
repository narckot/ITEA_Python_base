from string import whitespace, punctuation, ascii_letters, digits

enter_num = []
enter_char = []
filter_str = whitespace + punctuation + digits


def clear_word(enter_string, our_filter):  # ф-ция проверяет текст на латинские символы
    enter_char = []
    enter_list = list(enter_string)
    for i in range(0, len(enter_list)):
        if enter_list[i] in our_filter:
            continue
        if enter_list[i] not in ascii_letters:
            raise ValueError
        enter_char.append(enter_list[i])

    return enter_char


def bad_char(text):  # ф-ция проверяет текст на не латинские символы
    enter_list = list(text)
    for i in range(0, len(enter_list)):
        if enter_list[i] in filter_str:
            continue
        if enter_list[i] not in ascii_letters:
            enter_char.append(enter_list[i])
            enter_num.append(i)
    return enter_char, enter_num


if __name__ == "__main__":                            # ОСНОВНОЙ БЛОК
     needed_text = """stih from site Это кто упал? Серёжа?
                         Нет, не он, - его одёжа.
                         Что же стукнула одёжа?
                         В середине был Серёжа.
                         """

#if __name__ == "__main__":                          # ТЕСТОВЫЙ БЛОК НА ПРОВЕРКУ
#        needed_text = """stih from site"""

try:                                                # вызываем функцию clear_word
    enter_list = clear_word(needed_text , filter_str)
    print("\nПроверка на латинские символы пройдена. \nСПАСИБО!\n--------")

except ValueError:                                    # выводим результат поиска
    print("\n----- ERROR!!! -----\n")
    bad_list, bad_num = bad_char(needed_text)
    print(bad_list)
    print(bad_num)
    print("\n----- В тексте найдены символы не из английскго алфавита! -----\n\n")
    print("| {:^3}  | {:^5} |".format("Символ", "Порядковый номер"))
    print("|_________|__________________|")
    for i in range(0, len(bad_list)):
        print("| {:6}  | {:>16} |".format(bad_list[i], bad_num[i]))
