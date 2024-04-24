#cereating a set
s={1,2,3,4}
print(s)
print(type(s))
print('-'*50)

#adding AND  removing the elements
print(s)
s.add(5)
print(s)
print('-'*50)
#poping
popel=s.pop()
print(popel)
print('-'*40)

#delete
print(s)
s.discard(3)
print(s)

#iterate
for i in (s):
    print(i)

#checking the value
print(s)
print(2 in s)
print(3 in s)
print(4 in s)
print('-'*50)
#set operation
set1={1,2,3,4,5}
set2={4,5,6,7,8}
print('Union: ', set1 | set2)
print('Itersection: ', set1 & set2)
print('Difference:',set2-set1)
print('Difference:',set1-set2)
print('Symetric Diff:',set1^set2)
print('-'*30)
#clearing
print(s)
s.clear()
print(s)
print('-'*30)

#tuple instalization
tpl=(1,2,3,4,5)
print(tpl)
print('-'*30)

#accessing
tpl=(1,2,3,4,5)
print(tpl[0])
print('-'*30)
 
#slicing
tpl=(1,2,3,4,5)
print(tpl[1:3])
print('-'*30)

#concatenate
tpl1=(1,2,3,4)
tpl2=(4,5,6,7)
tpl=tpl1+tpl2
print(tpl)
print(len(tpl))
print(type(tpl))
print('-'*30)

#iterating
for i in tpl:
    print(i)
#checking the value
print(tpl)
print(2 in tpl)
print(3 in tpl)
print(4 in tpl)
print('-'*50)

#count
print('-'*50)
print(tpl.count(3))

#index
print('-'*50)
print(tpl.index(3))

#multiply
print('-'*30)
print(tpl*3)

print('-'*30)
lst1=[1,2,3,4,5,6]
print(lst1)
set1=set(lst1)
print(set1)
# dic1=dict(lst1)
# print(dic1)