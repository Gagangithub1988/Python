def fibo(n):
    a=0
    b=1
    sum=0
    if n<0:
        print("Incorrect input")
    elif n==0:
        return a
    elif n==1:
        return b
    else:
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            if b%2==0:
                sum+=b
        return sum
fibonacci=fibo(n=int(input("Enter a number: ")))
print(fibonacci)