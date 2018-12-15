from string import whitespace, punctuation

print('\nСейчас мы заполним слова в словарь для перевода, в конце мы увидим наш перевод'
      '\n------------------------------------------------------------------------------'
      '\n')

n = 0

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

    def trans_text(text, vocabr):  # функция переводит вводимый текст
        point = '.'
        comma = ','
        text = text.lower()
        for char in point:
            if char in text: text = text.replace(char, " . ")  # заменяем точку для красоты вывода
        for char in comma:
            if char in text: text = text.replace(char, " , ")  # заменяем пробел для красоты вывода
        list_text = text.split()
        vocabr.update([(".", "."), (",", ",")])  # добавляем в словарь точку и запятую
        for i in range(0, len(list_text)):
            if list_text[i] in vocabr:
                list_text[i] = vocabr[list_text[i]]  # переводим текст
        trantl_text1 = (" ".join(str(x) for x in list_text))
        print("--------------------------------------------------------")
        print("Перевод текста:   ", trantl_text1)  # Выводим перевод текста
        print("--------------------------------------------------------")
        return trantl_text1

    trans_text(text, fist_dict)

    # запрашиваем новый текст или выход из программы
    while new_text == "":
        new_text = input("Введите новый текст или exit для выхода из программы: ")
        if new_text == "":
            continue
        elif new_text != "exit":
            new_list = text_change(new_text)
            for i in range(0, len(new_list)):  # создаем новый словарь переводов
                if new_list[i] not in fist_dict:  # проверяем знакомо ли нам слово
                    fist_dict[new_list[i]] = get_translate(new_list[i])  # если слово не знакомо переводим его
            trans_text(new_text, fist_dict)
            new_text = ""

    return fist_dict


if __name__ == "__main__":
    vocabluary = {}
    text = """Здесь определяется текст на котором будет продемонстрирована правильность работы программы.
        Текст должен быть многострочным.
        В тексте должны быть пустые строки
        и использоваться знаки из whitespace, например """ + "\t" + """табуляция"""
    while text != "" and n == 0:
        vocabluary.update(get_vocabluary(text))  # переводим исходный текст


        def sort_vocab(sort_dict):  # функция сортирует словарь по слову - переводу
            list_vol = list(sort_dict.values())  # создаем список ключей
            list_keys = list(sort_dict.keys())  # создаем список значений
            # создаем копию словаря с поменяными значениями ключей и значений
            sort_copy = dict(zip(list_vol, list_keys))
            list_vol.sort()  # сортируем значения по алфавиту
            for i in range(0, len(list_vol)):  # создаём словарь из значений и None
                dict_copy = dict((i, None) for i in list_vol)
            for i in range(0, len(list_vol)):  # заполняем словарь значениями исходного словаря по ключам текущего
                dict_copy[list_vol[i]] = sort_copy[list_vol[i]]
            list_vol = list(dict_copy.values())
            list_keys = list(dict_copy.keys())
            # создаём cловарь с заменой местами значений ключей и значений
            dict_copy = dict(zip(list_vol, list_keys))
            return dict_copy


        vocabluary1 = sort_vocab(vocabluary)  # вызываем функцию сортировки по слову - переводу
        vocabluary1.pop(".")  # удаляем из словаря точку (для красоты вывода)
        vocabluary1.pop(",")  # удаляем из словаря пробелл (для красоты вывода)
        print("\n")
        print("| {:^30}  | {:^30} |\n".format("СЛОВО", "ПЕРЕВОД"))  # отображаем словарь переводов
        for key, value in vocabluary1.items():
            print("|  {:<30} | {:^30} |".format(key, value))
        n = 1
