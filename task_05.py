exit = 0
sum_finish = 0

while exit != 1:
    num = input('Введите числе через пробел, для выхода введите "Q": ').split()
    sum = 0

    for el in range(len(num)):
        if num[el] == 'Q':
            exit = 1
        else:
            sum = sum + int(num[el])
    sum_finish += sum
    print(f'Получилось: {sum_finish}')