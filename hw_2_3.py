string_1 = -1
string_2 = 1
result = 1
while string_1 < 0 or result != 0:
    string_1 = float(input("Введите число для вывода факториала: "))
    result = string_1 % 1
    if result != 0:
        print("\n-----\nERROR\n-----\nДолжно быть целое число.\n")
    if string_1 < 0:
        print("Число должно быть > или = 0")
string_1 = int(string_1)
for i in range(1, string_1 + 1):
    string_2 = string_2 * i
print("Факториал: ", string_1, "! = ", string_2)
