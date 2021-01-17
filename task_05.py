my_list = [7, 5, 3, 3, 2]

print('Для остановки введите: 999')
stat = 0
while stat !=999:
    n = 0
    print(f"Рейтинг - {my_list}")
    stat = int(input('Введите новое значение рейтинга: '))
    for i in my_list:
        if my_list[n] < stat:
            my_list.insert(n, stat)
            break
        elif my_list[len(my_list) - 1] >= stat:
            my_list.insert(len(my_list), stat)
            break
        n += 1