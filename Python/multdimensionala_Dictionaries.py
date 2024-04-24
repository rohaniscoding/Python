dct={1:{'name':'Rohan','phone':8279601296},
      2:{'name':'Dhruv','phone':8279701296},
      3:{'name':'RIYA','phone':82794201296},}
print(dct)
print('-'*50)

#Accessing the Elements
print(dct)
print(dct[1])
print(dct[1]['name'])
print('-'*50)

#Adding, Updating &deleting
#adding
dct[4]={'name':'vfx','phone':8279601296}
print(dct[4])
print('-'*50)
#updating
dct[3]['name']='Avneet'
print(dct)
print('-'*50)
#Deleting
print(dct)
del dct[3]
print(dct)
print('-'*50)

#iteration
print(dct)
for k in dct.keys():
    print (k,dct[k]['name'],dct[k]['phone'])
# n=input('Enter the Key value You want to search for')
# if(n in dct):
#     print('Key One is in the Dictionary')
# else:
#     print('Key is Not in the list')

print('-'*50)

#going a level deeper with marks
data ={ 1:{'name':'Rohan','phone':8279601296,'marks':{'hindi':92,'math':99,'science':97}},
        2:{'name':'Dhruv','phone':8279701296,'marks':{'hindi':29,'math':39,'science':37}},
        3:{'name':'RIYA','phone':82794201296,'marks':{'hindi':42,'math':39,'science':57}}}
print(data)

print('-'*50)

for i in data.keys():
    print(i,data[i]['name'],data[i]['marks']['math'])
