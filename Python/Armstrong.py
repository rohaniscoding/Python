def isar(number):
    numdigit=len(str(number))
    sum=0
    temp=number
    while temp>0:
        digit=temp%10
        sum+=digit** numdigit
        temp=temp//10
    if number==sum:
     return True
    else:
     return False

num=int(input('Enter The NUmber'))   
res=bool(isar(num))
if res :
    print('Number is Armstong')
else:
    print ('NUmber is not Armstrong')
