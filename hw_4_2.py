from string import punctuation, ascii_letters, digits, whitespace

our_filter = whitespace + punctuation + digits
enter_char = []
filt2 = punctuation + digits + '\t\n\r\x0b\x0c'
ascii_lettersflt = ascii_letters + " "


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


def bad_char(needed_text):  # функция проверяет текст на символы не из английского алфавита
    needed_text = needed_text.lower()
    enter_list = list(needed_text)
    for i in range(0, len(enter_list)):
        if enter_list[i] in filt2:  # пропускаем специальные символы и символы пунктуации
            continue
        if enter_list[i] in ascii_lettersflt:
            enter_char.append(enter_list[i])  # добавляем в список отобранных символов
    new_str = ("".join(str(x) for x in enter_char))
    new_str = new_str.split(" ")
    new_str.sort()
    while new_str[0] == "":
        new_str.remove("")
    return new_str


if __name__ == "__main__":
    needed_text: str = """stih from site Это кто упал? Серёжа?
                         Нет, не он, - его одёжа.
                         Что же стукнула одёжа?
                         В середине был Серёжа."""
    print("\nИсходный текст: ", needed_text)
try:
    enter_list = clear_word(needed_text, our_filter)  # вызываем ф-цию clear_word
    print("\nПроверка на латинские символы пройдена. \nСПАСИБО!\n--------")

except ValueError:  # выводим результат поиска
    print("\n----- В тексте найдены символы не из английскго алфавита! -----\n\n")
    bad_list = set(bad_char(needed_text))
    print("Очищенный текст: ", bad_list)
