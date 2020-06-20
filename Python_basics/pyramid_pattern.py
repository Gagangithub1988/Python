def pyramid_pattern(n):
    num=1
    k = 2 * n - 2

    for i in range(0, n):
        #for num in range(1, 10):
        num=1+i
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i+1):
            print(num, end=" ")
        print("\r")

n = 5
pyramid_pattern(n)