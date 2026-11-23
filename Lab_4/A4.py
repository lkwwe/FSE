def isValidNumber(string):
    return string.isdigit() and len(string) in [13, 15, 16]

def getCheckSum(string):
    CheckSum = 0
    for i in range(len(string)-2, -1, -2):
        if int(string[i])*2 > 9:
            CheckSum = CheckSum + 1 + int(string[i])*2 - 10
        else:
            CheckSum = CheckSum + int(string[i])*2
    for i in range(len(string)-1, -1, -2):
        CheckSum += int(string[i])
    return CheckSum

def getCardType(string):
    if (len(string)==13 or len(string)==16) and string.startswith("4"):
        return "Visa"
    if len(string)==15 and string.startswith(("34", "37")):
        return "American Express"
    if len(string)==16 and string.startswith(("51", "52", "53", "54", "55")):
        return "Master Card"
    return "Invalid"

CardNumber = input("Введите номер банковской карты: ")
if isValidNumber(CardNumber):
    if getCheckSum(CardNumber) % 10 == 0:
        print (getCardType(CardNumber))
    else: 
        print ("Invalid")
else:
    print ("Invalid")
