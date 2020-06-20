def histogram(item):
    for n in item:
        output = ''
        times = n
        while(times>0):
            output+="*"
            times=times-1
        print(output)
histogram([2,3,4,7])