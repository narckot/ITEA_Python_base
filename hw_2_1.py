string_1 = ''
while string_1 == '' or string_1 == '0':
    string_1 = input("Введите 1-e число: ")
string_1 = float(string_1)
string_2 = float(input("Введите 2-е число: "))
string_3 = float(input("Введите 3-е число: "))

if string_2 < 0 < string_3 and string_1 != 0:
    print("{} (X**2) {} x + {} = 0".format(string_1, string_2, string_3))
elif string_2 < 0 and string_3 < 0 and string_1 != 0:
    print("{} (X**2) {} x {} = 0".format(string_1, string_2, string_3))

elif string_2 < 0 < string_3 and string_1 == 0:
    print("{} x + {} = 0".format(string_2, string_3))
elif string_2 < 0 and c < 0 and string_1 == 0:
    print("{} x {} = 0".format(string_2, string_3))
elif string_2 < 0 and string_1 != 0 and string_3 == 0:
    print("{} (X**2) {} x = 0".format(string_1, string_2))

if string_1 == 0 and string_3 == 0:
    print(string_2, "x=0")


if string_2 > 0 and string_3 > 0 and string_1 != 0:
    print("{} (X**2) + {} x + {} = 0".format(string_1, string_2, string_3))
elif string_2 > 0 > string_3 and string_1 != 0:
    print("{} (X**2) + {} x {} = 0".format(string_1, string_2, string_3))

elif string_2 > 0 < string_3 and string_1 == 0:
    print("{} x + {} = 0".format(string_2, string_3))
elif string_2 > 0 > string_3 and string_1 == 0:
    print("{} x {} = 0".format(string_2, string_3))

elif string_2 > 0 and string_1 != 0 and string_3 == 0:
    print("{} (X**2) + {} x=0".format(string_1, string_2))

elif string_2 == 0 and string_3 == 0:
    print(string_1, "(x**2) = 0")


diskrem = string_2**2 - 4 * string_1 * string_3
print("Дискриминант:\n", diskrem)

x1 = (-string_2 + diskrem**(1/2))/(2 * string_1)
x2 = (-string_2 - diskrem**(1/2))/(2 * string_1)

if diskrem < 0:
    print("Уравнение имеет комплексные корни:\n Z_1 = ", x1, "\n Z_2 = ", x2)
elif diskrem == 0:
    print("Уравнение имеет один корень: \n", "Z = ", x1)
else:
    print("Корни уравнения:\n x1 = ", x1, "\n Z_2 = ", x2)
