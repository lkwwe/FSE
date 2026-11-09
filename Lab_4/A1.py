import random
import time

N = int(input('Введите количество примеров:'))
all_time = 0
correct_answer = 0

for i in range(N):
    print (f'Вопрос {i+1}/{N}')
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    start_time = time.time()
    while True:
        try:
            answer = int(input(f'{a} × {b} = '))
            break
        except ValueError:
            print('Пожалуйста, введите целое число!')

    time_spend = time.time() - start_time
    if answer == a*b:
        print (f'Верно! (Время: {time_spend:.2f})')
        correct_answer += 1 
    else:
        print (f'Неверно! Правильно: {a*b} (Время: {time_spend:.2f})')
    all_time += time_spend
print (50*'=')
print ('СТАТИСТИКА:')
print (50*'=')
print(f'Общее время: {all_time:.2f}')
print (f'Среднее время на вопрос: {(all_time/N):.2f}')
print (f'Правильных ответов: {correct_answer}/{N}')
print (f'Процент правильных: {(correct_answer/N*100):.2f}%')
