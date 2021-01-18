my_str = input('Введите данные через пробел: ')
n = 0
for i in my_str.split():
    print(f'{n+1}: {my_str.split()[n][0:10]}')
    n += 1