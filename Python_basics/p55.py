def decor(func):
    def inner(name):
        if name=="Sunny":
            print("Hello Sunny bad morning")
        else:
            func(name)
    return inner
@decor
def wish(name):
    print("Hello",name,"good morning")
decorfunction =decor(wish)
wish("Sunny")
wish("Gagan")
decorfunction("Sunny")
