from string import punctuation, whitespace

moduls = whitespace + punctuation

print('Привет!\n'
      '1. Программа формирует словарь отсортированные по алфавиту. \n'
      '2. Пустая строка означает завершение программы.\n'
      '_______________________________________________________________________________________________________________________________')


def enter_list():
    my_list = [" "]
    enter_string = "d"
    while enter_string != [""]:
        enter_string = (input("Введите строку:  ")).lower()
        if enter_string == "":
            print("----------------------"
                  "\nВы прервали программу!")
        for char in moduls:
            enter_string = enter_string.replace(char, " ")
        enter_string = enter_string.split(" ")
        my_list = my_list + enter_string
    return my_list


word = enter_list()
word.sort()
while word[0] == "":
    word.remove("")
word.remove(" ")
long_word = len(word)
if long_word < 1:
    print("Вы не ввели слов для статистики!")
if long_word != 0:
    print("----------------------")
    print("Слова из текста отсортированные по алфавиту: ")
    print(word)
