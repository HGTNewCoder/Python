# Pytago: a^2 + b^2 = c^2
# Enter a number (X)
# Print Pytago form of X (a,b,c)
# Print 0 if can't make Pytago form of X

def Pytago(x):
    answer=[]
    for a in range (1, x):
        for b in range (2, x):
            for c in range (3, x):
                if (a + b + c == x and a*a + b*b == c*c):
                    answer.append([a, b, c])
                else:
                    answer = 0
                    break
    print(answer)
Pytago(12)