from string import whitespace, punctuation

print('\nСейчас мы заполним слова в словарь для перевода, в конце мы увидим наш перевод'
      '\n------------------------------------------------------------------------------'
      '\n')

a = 0

moduls = whitespace + punctuation


def get_vocabluary(text):  # перевод инпута в словарь для перевода

    def get_translate(word):  # функция перевода слова
        enter_string = ""
        punctuation_simbol = '"""&\()*+,!"#$%-./:;<=>?@[\\]^_`{|}~'
        whitespace_simbol = '\n\r\x0b\t\x0c'
        moduls = whitespace_simbol + punctuation_simbol
        while enter_string == "":
            print('Слово "', word, '" не известною')
            enter_string = (input("Введите перевод слова на английский или русский язык:  ")).lower()
            enter_string.lower()
            for char in moduls:
                if char in enter_string:
                    enter_string = ""
        return enter_string

    def text_change(text):  #ф-ция возвращает список слов
        text = text.lower()
        for char in whitespace:  #ф-ция убирает лишние символы
            if char in text:
                text = text.replace(char, " ")
        for char in punctuation:  #ф-ция убирает спец. символы
            if char in text:
                text = text.replace(char, " ")
        text = text.split(" ")
        text.sort()  #сортировка по алфавиту
        while text[0] == "":
            text.remove("")
        return text

    fist_text = text_change(text)

    def get_vocab(fist_text):  #ф-ция создает словарь преводов
        for i in range(0, len(fist_text)):  #преобразовываем список слов из текста в словарь
            result = dict((i, None) for i in fist_text)
        for i in range(0, len(fist_text)):  #проверка вводимых слов
            if result.get(fist_text[i]) is None:  #если проверка не прошла - запускаем функцию перевода слова
                result[fist_text[i]] = get_translate(fist_text[i])
        return result

    fist_dict = get_vocab(fist_text)
    new_text = ""
    # запрашиваем новый текст или выход из программы
    while new_text == "":
        new_text = input("Введите новый текст или exit для выхода из программы: ")
        for char in punctuation:
            if char in new_text or char == "":
                new_text = ""
        if new_text == "":
            continue
        elif new_text != "exit":
            new_list = text_change(new_text)
            for i in range(0, len(new_list)):  # создаем новый словарь переводов
                if new_list[i] not in fist_dict:  # проверяем знакомо ли нам слово
                    fist_dict[new_list[i]] = get_translate(new_list[i])  # если слово не знакомо переводим его
            new_text = ""
    return fist_dict


if __name__ == "__main__":
    vocabluary = {}
    text = """Здесь определяется текст на котором будет продемонстрирована правильность работы программы.
    Текст должен быть многострочным.
    В тексте должны быть пустые строки
    и использоваться знаки из whitespace, например """ + "\t" + """табуляция"""
    while text != "" and a == 0:
        vocabluary.update(get_vocabluary(text))  # переводим исходный текст
        print("\n")
        print("| {:^30}  | {:^30} |\n".format("СЛОВО", "ПЕРЕВОД"))  # cловарь с переводом
        for key, value in vocabluary.items():
            print("|  {:<30} | {:^30} |".format(key, value))
        a = 1
