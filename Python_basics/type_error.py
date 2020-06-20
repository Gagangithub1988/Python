def integer_type(a,b):
    if not(isinstance(a,int) and isinstance(b,int)):
        raise TypeError("Inputs must be integer")
    return a+b
print(integer_type(3,8))