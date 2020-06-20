def new_string(str,n):
    result = ""
    for i in range(n):
        if len(str)>2:
            result=result+str[:2]

        else:
            result = result+str
    return result
print(new_string("Gagan",5))

