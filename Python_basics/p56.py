def mygen():
    yield "A"
    yield "B"
    yield "C"
g=mygen()
for x in g:
    print(x)