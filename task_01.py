def calc():
    try:
        numerator = float(input("Введите числитель: "))
        denominator = float(input("Введите знаменатель: "))
        amount = numerator / denominator
    except ValueError:
        return 'Ошибка. Не корректное число!'
    except ZeroDivisionError:
        return 'Ошибка. Делить на 0 нельзя'

    return amount

print(calc())