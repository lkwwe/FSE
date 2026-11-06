import string
password = (input())

allowed1 = '*-#'
allowed2 = string.ascii_lowercase + string.ascii_uppercase + string.digits + '*-#'

if len(password)!=8:
    print ('Длина пароля не равна 8')
elif password==password.lower():
    print ('В пароле отсутствуют заглавные буквы')
elif password==password.upper():
    print ('В пароле отсутствуют строчные буквы')
elif not any(symbol.isdigit() for symbol in password):
    print('В пароле отсутствуют цифры')
elif not any (symbol in allowed1 for symbol in password):
    print ('В пароле отсутствуют специальные символы')
elif not all(symbol in allowed2 for symbol in password):
    print ('В пароле используются непредусмотренные символы')
else: 
    print ('Надежный пароль')
