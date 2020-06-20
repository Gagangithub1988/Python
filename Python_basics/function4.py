def fun(n):
    return ((abs(1000-n))<=100 or (abs(2000-n))<=100)
print(fun(1200))

def sum(a,b,c):
    sum=a+b+c
    if a==b==c:
        sum=sum*3
        print("The sum is: ",sum)
    else:
        print("The sum is ",sum)

sum(2,3,4)
sum(3,3,3)