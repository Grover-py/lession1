def people(first_name, second_name, year_start, citi, email, num_phone):
    print(f'перед нами {first_name}, {second_name} {year_start} года рождения, проживающий в городе {citi}. Контактная информаия :{email}, {num_phone}')

first_name = input('Введите Имя: ')
second_name = input('Введите Фамилию: ')
year_start = input('Введите год рождения: ')
citi = input('Введите город проживания: ')
email = input('Введите Email: ')
num_phone = input('Введите номер телефона: ')

people(first_name.title(), second_name.title(), year_start, citi.title(), email, num_phone)