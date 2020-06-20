a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
if a>b:
    print("invalid")
elif a<=0 or b<=0:
    print("invalid")
else:
    for x in range(10):
        a=a+b
        b=b+10
        print("Value of a and b: ",a,b)