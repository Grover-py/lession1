my_str = input('Введите данные через пробел: ')
my_list = my_str.split()

n = 0
for i in my_list:
    print(f'{n+1}: {my_list[n][0:10]}')
    n += 1