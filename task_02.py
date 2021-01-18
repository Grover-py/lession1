time = int(input(f'Введите время в секундах: '))

h = time//3600
m = (time//60)%60
s = time%60

if m<10:
    m='0'+str(m)
else:
    m=str(m)
if s<10:
    s='0'+str(s)
else:
    s=str(s)

print(f'в нормальном формате это будет - {h}:{m}:{s}')