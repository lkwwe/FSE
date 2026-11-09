n = int(input('Введите количество строк n: '))
m = int(input('Введите количество столбцов m: '))
ch = input('Выберите печатаемый символ: ')

print (f'ПРЯМОУГОЛЬНИК {n}х{m}:')
for i in range(n):
    for j in range(m):
        print (f'{ch}', end='')
    print()

print (f'ПРАВЫЙ ТРЕУГОЛЬНИК:')
x = 0
for i in range(n):
    print((i+1)*f'{ch}', end='' )
    print()

print (f'РАМКА {n}x{m}: ')
y = m - 2
for j in range(m):
    print (f'{ch}', end='')
print()
for i in range(n-2):
    print (f'{ch}', end='')
    print (y*' ', end='')
    print (f'{ch}', end='')
    print()
for j in range(m):
    print (f'{ch}', end='')
