num_start = ""
num_end = ""
result = 0
num_finish = 1
while num_start == "" or num_finish != 0:
    num_start = ""
    num_start = input("Введите 1е целое число:  ")
    if num_start == "":
        continue
    num_start = float(num_start)
    if num_start < 0:
        print("Число должно > или = 0")
        continue
    num_finish = num_start % 1
    if num_finish != 0:
        print("Должно быть целое число")
        continue
num_start = int(num_start)
num_finish = 1
while num_end == "" or num_finish != 0:
    num_end = ""
    num_end = input("Введите 2е целое число:  ")
    if num_end == "":
        continue
    num_end = float(num_end)
    if num_end < num_start:
        print("Число должно быть > или = второму числу")
        continue
    num_finish = num_end % 1
    if num_finish != 0:
        print("Число должно быть целым числом")
        continue
num_end = int(num_end)
print("Начало ряда - ", num_start)
print("Конец ряда - ", num_end)
for i in range(num_start, num_end + 1):
    result = i + result
    i += 1
print("Сумма чисел выбранного диапазон: ", result)
