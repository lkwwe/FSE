x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

if (x1>0 and y1>0):
    res1 = 'I'
elif (x1>0 and y1<0):
    res1 = 'IV'
elif (x1<0 and y1>0):
    res1 = 'II'
else:
    res1 = 'III'

if (x2>0 and y2>0):
    res2 = 'I'
elif (x2>0 and y2<0):
    res2 = 'IV'
elif (x2<0 and y2>0):
    res2 = 'II'
else:
    res2 = 'III'

if res1==res2:
    print ('Yes,', res1)
else: 
    print ('No')
