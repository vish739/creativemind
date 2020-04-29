def smart_divide(func):
    def inner(a,b):
        print(a,b)
        if (b==0):
            print("b can not be 0")
            return
        return func(a,b)
    return inner

@smart_divide
def divide(a,b):
    return a/b

print(divide(3,0))