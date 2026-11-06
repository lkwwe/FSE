x1 = int(input())
x2 = int(input())

if x2>x1:
    V = x2-x1
else:
    V = 10000 - x1 + x2

if V<=300:
    sum = 21
elif V>300 and V<=600:
    sum = 21 + (V-300)*0.06
elif V>600 and V<=800:
    sum = 39 + (V-600)*0.04
else:
    sum = 47 + (V-800)*0.025

price = sum/V

print (f'{"Предыдущее":^16}{"Текущее":^16}{"Использовано":^16}{"К оплате":^16}{"Ср. цена m^3":^16}')
print (f'{x1:^16}{x2:^16}{V:^16}{sum:^16.2f}{price:^16.2f}')
