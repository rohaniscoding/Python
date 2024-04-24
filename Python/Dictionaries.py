dct={1:'Rohan',2:'dhruv',3:'sachin',4:'ankur',3:'hacker'}
print(dct)

print(dct[1])
print(dct[2])
print(dct.get(1))
print('-'*20)
#adding and updating key values
print(dct)
dct[6]='Sachin'
print(dct)
dct[6]='Prakash'
print(dct)
del dct[6]
print(dct)
print('-'*20)

#cleaning the dictionary
print(dct)
dct.clear()
print(dct)
print('-'*20)

#iterate the dictionary
dct={1:'Rohan',2:'dhruv',3:'sachin',4:'ankur',3:'hacker'}
print(dct.keys())
print(dct.values())

for k in dct.keys():
    print(k,dct[k])

print(dct.items())
for k,v in dct.items():
    print(k,v)
print('-'*20)

#check if key is present
print(dct)
print(1 in dct) 
print('1' in dct)

#updating the ditionary
print('_'*20)
dct1={1:'A',2:'B',3:'C'}
dct2={1:'a',2:'b',3:'c'}
print(dct1)
print(dct2)
dct1.update(dct2)
print(dct1)
print(dct2)
# print(dct1 + dct2)
