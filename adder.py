def inc(func):
    def vishal(a):
        a=a+1
        return func(a)
    return vishal

def dec(func):
    def vishal(a):
        a=a-1
        return func(a)
    return vishal

@dec
@inc
def pract(a):
    print(a)

pract(4)

