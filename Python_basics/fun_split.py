def greenTicket(a,b,c):
    if a==b==c:
        print("The result is ",20)
    elif a==b or a==c or b==c:
        print("The result is ", 10)
    else:
        print("The result is ", 0)

a,b,c=input("Enter the a,b,c value: ").split(",")
#b=int(input("Enter the b value: "))
#c=int(input("Enter the c value: "))
greenTicket(a,b,c)