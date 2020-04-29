def validate(func):
    def inner(**a):




            if ((a[keys])==""):
                print("values can not be blank")
                return
        for keys in a:
            if (keys == " "):
                print("keys can not be blank")
                return

            return func(**a)
    return inner


@validate
def add_student(**kwargs):
    student_info=kwargs
    print(student_info)

d={'1': 'vishal',
   '2': 'abc',
   '': 'pqr'}
add_student(**d)