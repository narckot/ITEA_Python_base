name = (input('Введите имя и фамалию: '))
print('Здравствуй ', name, '!')
print('')
itea_day = int(19)
itea_month = int(11)
itea_year = int(2018)

b_day = int(input('Введите Ваш день даты рождения: '))
month = int(input('Введите Ваш месяц даты рождения: '))
year = int(input('Введите Ваш год даты рождения: '))

month = (year * 12 + month)
b_day = (month * 30 + b_day)

itea_month = int(itea_year * 12 + itea_month)
itea_day = int(itea_month * 30 + itea_day)
itea_date = int((2018 * 360) + (11 * 30) + 19)

sum_day = int(itea_date - b_day)
sum_month = int((itea_date - b_day) / 30)
sum_year = int((itea_date - b_day) / 360)

print('')
print('Вы прожили лет до начала курса:  ', sum_year)
print('Вы прожили месяцев до начала курса:  ', sum_month)
print('Вы прожили дней до начала курса:  ', sum_day)
