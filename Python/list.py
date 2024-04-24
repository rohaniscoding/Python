lst=['Rohan ','Ankkur','dhruv','sachin']
print(lst)
#Access the elements through indexing
print(lst[0])
print(lst[-1])
print(lst)
# Modify the value
lst[2]='Sakshi'
print(lst)

#slicing
print(lst[1:3])

#reverse a string
print(lst[::-2])

#append
print(lst)
lst.append('Ankit')
print(lst)

#removing the values
print(lst)
lst.remove('Ankit')
print(lst)

#length of list
print(lst)
print(len(lst))

#sorting
lst=[3,5,6,7,4,2,8,1,9,0]
print(lst)
print(sorted(lst))
print(lst.reverse())

#find the element
lst=['Rohan ','Ankkur','dhruv','sachin']
print(lst.index('dhruv'))

#count the element
lst=['Rohan ','Ankkur','dhruv','sachin']
print(lst.count('Rhan'))

#extend the list
print(lst)
lst.extend(['Palak','Mansha','Priya'])
print(lst)

#min max
lst=[3,5,6,7,4,2,8,1,9,0]
print(lst)
print(min(lst))
print(max(lst))

#2ways to access list

#iterating through the elemenst
print(lst)
for i in lst:
    print(i,end=' ')
print(sorted(lst))

#indexing
print(lst[0])
for i in range(len(lst)):
    print(i,lst[i])

#iterating the list in reverse
for i in range(len(lst)-1,-1,-1):
    print(lst[i])
 