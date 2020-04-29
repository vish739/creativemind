def smart_multiply(func):
    def inner(*kargs):
        n=kargs
        for i in n:
            if (i==0):
                raise Exception("Sorry, no numbers zero")
                return
        return func(*kargs)
    return inner

@smart_multiply
def mul(*kargs):
    number=kargs
    print(number)
    mul=1
    for i in number:
        mul=mul*i
    print(mul)

mul(3,4,0)


