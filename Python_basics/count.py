n=int(input("enter a number: "))
count=0
while n>0:
    count+=1
    n//=10
print("The number of digits in entered number:",count)