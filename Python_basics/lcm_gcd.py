def gcd(x, y):
    while(y):
        x, y = y, x % y
        #print(x,y)
    return x

def lcm(x, y):
   lcm = (x*y)//gcd(x,y)
   return lcm


n1 = int(input("Enter the number: "))
n2 = int(input("Enter the number: "))
print("LCM:", lcm(n1, n2))
print("GCD:",gcd(n1, n2))