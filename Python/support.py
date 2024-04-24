def greet(name = '------'):
    print('Hello'+name)

def subm(a=0,b=0):
    return a+b

def arth(a=0,b=0):
    return a+b,a-b,a*b

def sq(lst):
    return(i**2 for i in lst)

def cube(lst):
    return(i**3 for i in lst)

def finals(lst):
    lst_1=sq(lst)
    lst_2=cube(lst)
    return[lst_1[i]+lst_2 for i in range(len(lst_1))]