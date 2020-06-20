from math import gcd
str="Gagan"
print(str)
print(str[::-1])
#print("".join(reversed(str)))
i=len(str)-1
target=''
while(i>=0):
    target = target+str[i]
    i=i-1

print(target)

print(gcd(12,8))
print(lcm(12,8))
