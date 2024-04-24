lst=[[1,2,3],[4,5,6],[7,8,9]]
print(lst)
# lst.extend(['Rohan',25])
# print(lst[3])

#accesing the list
print(lst)
print(lst[0][0])
print(lst[2][2])
print(lst[2])
print('-'*12)
#modify the values
print(lst)
lst[1][1]=9
print(lst)
lst[1]=['Rohan',25]
print(lst)
print('-'*12)

#delete the index
print(lst)
print(len(lst))
del lst[0]
print(lst)
print(len(lst))
 
#modifying the values
lst=[1,2,3,4,5,[1,2,3],6]
print(lst)
print('-'*12)

#reverse the string
lst=[[1,2,3],[4,5,6],[7,8,9]]
print(lst)
print(lst[::-1])
print('-'*20)
#accessing all the values
lst=[[1,2,3,],[4,5,6],[7,8,9]]
print(lst)
for i in lst:
    for j in i:
        print(j)
print('-'*20)