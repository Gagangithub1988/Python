n=int(input("Enter a number: "))
def hailstone(n):

    count = 1
    if n > 1:
        if n % 2 == 0:
            y=n//2
            print("{} is even so i take half: {}".format(n,y))
            count += hailstone(n // 2)
            #print(n)
        else:
            x=(n * 3) + 1
            print("{} is even so i take half: {}".format(n, x))
            count += hailstone((n * 3) + 1)
    return count

result = hailstone(n)
print(result)