start = int(input('Сколько километров вы пробегаете на данный момент: '))
end = int(input('Сколько километров вы бы хотели пробегать?: '))
day = 0

while start < end:
    start += start/10
    day = day + 1

print(f'Дней до достижения результата осталось: {day}')