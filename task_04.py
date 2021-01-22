x = int(input('Введите число: '))
y = int(input('Введите степень: '))

def my_func(x, y):
    sum = x
    n = 1
    if y > 0:
        while n != y:
            sum = sum * x
            n += 1
    elif y < 0:
        n = -1
        while n != y:
            sum = sum * x
            n -= 1
        sum = 1/sum
    else:
        sum = 1

    return sum

print(my_func(x,y))