def greet():
    for i in range(5):
        print('Hello')
greet()
print('-'*50)
 
#scope pof varible
gval=10
def greet1():
    lval=5
    print(gval+lval)
    print("global Variable Here")
greet1()
print('-'*50)

def subm(a,b):
    print(a,b,a+b)
subm(15,20)
print('-'*50)

def subm(a=0,b=0):
    print(a,b,a+b)
subm()
print('-'*50)

def subm(a=0,b=0):
    print(a,b,a+b)
subm(15,5)
print('-'*50)

#calling different functions
lst=[1,2,3,4,5]
def sq(lst):
    return[i**2 for i in lst]
def cu(lst):
    return[i**3 for i in lst]
def final(lst):
    lst1=sq(lst)
    lst2=cu(lst)

    return[lst1[i]+lst2[i] for i in range(len(lst1)) ]

print(sq(lst))
print(cu(lst))
print(final(lst))

