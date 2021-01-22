def int_func(*args):
    return (str(args[0]).title())

my_string = input('Введите слова в строчку: ')
print(int_func(my_string))
