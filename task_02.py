lot = int(input('Сколько элементов будет в списке: '))
my_list = list()

for i in range(lot):
    my_list.append(input(f'Введите значение элемента № {i+1}: '))

n_el = 0
for m in range(int(len(my_list)/2)):
    my_list[n_el], my_list[n_el + 1] = my_list[n_el + 1], my_list[n_el]
    n_el += 2

print(my_list)