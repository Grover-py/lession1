month = int(input('Введите номер месяца: '))

season_l = ['Зима', 'Весна', 'Лето', 'Осень']
season_d = {0 : "Зима",
             1 : "Весна",
             2 : "Лето",
             3 : "Осень"}

if month == 12 or month == 1 or month == 2:
    print(season_l[0])
    print(season_d.get(0))
elif 3 <= month <= 5:
    print(season_l[1])
    print(season_d.get(1))
elif 6 <= month <= 8:
    print(season_l[2])
    print(season_d.get(2))
elif 9 <= month <= 11:
    print(season_l[3])
    print(season_d.get(3))
else:
    print('В году всего 12 месяцев')