import  math
x=10.8
print(math.ceil(x))
print(math.floor(x))
print(math.trunc(x))
print('-'*30)
x=3
print(math.exp(x))
print(math.log(x))
print('-'*30)
x=90
print(math.sin(x))
print(math.cos(x))
print(math.tan(x))
print('-'*30)
print(math.pi)
print(math.e)

print(math.factorial(10))
print('-'*30)
#random
import random 
# random.seed(40)
print(random.random())
print(random.randint(1,11))
print(random.choice([1,2,3,4,5]))
print(random.sample([1,2,3,4,5],3))
print(random.uniform(1.0,3.0))
print('-'*30)

#data And Time
import datetime
print(datetime.datetime.now())
print(datetime.datetime(2024,3,21,17,55,20))
print(datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S"))
date_1=datetime.datetime(2024,3,21,17,55,20)
date_2=datetime.datetime.now()
diff=date_2 - date_1
print(diff)

#Collection
from collections import Counter, defaultdict, OrderedDict
lst=[1,2,3,4,5,6,7,8]
print(Counter(lst))
print('-'*30)
d=defaultdict(int)
d['a']+=2
print(d)
print('-'*30)

d= OrderedDict()
d['one']=1
d['two']=2
print(d)
print('-'*30)

#string
import string
str='Rohan123abc'
for i in str:
    if(i not in '1234567890'):
        print(i)
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print(string.punctuation)
print('-'*30)

    
