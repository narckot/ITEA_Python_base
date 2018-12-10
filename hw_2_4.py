string = 0
result_a = 0
result_b = 1
while string <= 0 or result_finish != 0:
    string = float(input("Введите число Фибоначчи: "))
    result_finish = string % 1
    if result_finish != 0:
        print("Число должно быть целым.")
    if string <= 0:
        print("Число должно быть > 0.")
string = int(string)
for i in range(0, string + 1):
    result_a = result_a + result_b
    result_b = result_a - result_b
print("Результат числа Фибоначчи: ", string, " = ", result_b)
