a = int(input("Enter a: "))
b = int(input("Enter b: "))

def gcd1(a, b):
    if a == 0 or b == 0:
        return a + b
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    print(a)

def gcd2(a,b):
    if b == 0:
        gcd = a
        print(gcd)
        return gcd
    return gcd2(b, a % b)

gcd2(a, b)