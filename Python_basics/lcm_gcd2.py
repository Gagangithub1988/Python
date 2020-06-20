def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while (True):
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm


def gcd(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i
            #print(gcd)
    return gcd

n1 = int(input("Enter the number: "))
n2 = int(input("Enter the number: "))
print("LCM:", lcm(n1, n2))
print("GCD:",gcd(n1, n2))