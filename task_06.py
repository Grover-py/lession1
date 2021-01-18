my_list = []
product = {'название' : None,
             'цена' : None,
             'кол-во' : None,
             'ед. измерения' : None}
analitic = {'название' : [],
             'цена' : [],
             'кол-во' : [],
             'ед. измерения' : []}
action = None
n = 1
while action != 3:
    action = int(input('добавить товар: "1", вывести аналитику: "2", закончить цикл: "3": '))
    if  action == 1:
        analitic['название'].append(input('Введите название товара: '))
        analitic['цена'].append(input('Введите цену товара: '))
        analitic['кол-во'].append(input('Введите кол-во товара: '))
        analitic['ед. измерения'].append(input('Введите единицу измерения товара: '))

    elif action == 2:
        print(analitic)

    else:
        print('Что то пошло не так. Попробуйте ещё раз.')
