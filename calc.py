import math
a = int(math.pow(2, 2))

firstValue = 0
secondValue = 0
lastValue = 0
x = 0

for i in range(0, 3): #End + 1
    x = math.pow(10, i) 
    firstValue = firstValue + x

for k in range(0, 3):
    for i in range(0, k+1):
        x = math.pow(10, i)
        secondValue = secondValue + x

    
print("First Value: ", firstValue)
print("Second Value: ", secondValue)
print("Last Value: ", lastValue)


#firstValue: 111
#secondValue: 122