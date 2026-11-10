packets = input()
if not all (char in '01' for char in packets):
    print("Неверный ввод. Используйте только символы '0' и '1'!")
else:
    len = len(packets)
    len0 = packets.count('0')
    
    max_len0 = 0
    MAX_len0 = 0
    for packet in packets:
        if packet == '0':
                max_len0 +=1
                if max_len0 > MAX_len0:
                    MAX_len0 = max_len0
        else:
            max_len0 = 0

    precent = len0/len*100
    if precent <= 1:
        result = 'отличное качество'
    elif (precent > 1 and precent <= 5):
        result = 'хорошее качество'
    elif (precent > 5 and precent <= 10):
        result = 'удовлетворительное качествo'
    elif (precent > 10 and precent <= 20):
        result = 'плохое качествo'
    else:
        result = 'критическое состояние сети'

    print (f'Общее количество пакетов: {len}')
    print (f'Количество потерянных пакетов: {len0}')
    print (f'Длина самой длинной последовательности потерянных пакетов: {MAX_len0}')
    print (f'Процент потерь: {precent:.2f}%')
    print (f'Качество связи: {result}')
