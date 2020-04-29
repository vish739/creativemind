def smart_average(func):
    def inner(*args):
        print(" this is smart average")
        le=len(args)
        if (le==0):
            print("list is empty")
    return inner

@smart_average
def average(*kargs):
    arr=kargs
    sum=0
    n=len(arr)
    #print(arr)
    #print(type(arr))
    #print(n)
    for i in arr:
        sum=sum+i
    print(sum)



average(6,4,3,7,8,9,6,3)
average
