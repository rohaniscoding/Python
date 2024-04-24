dct={i:i**3 for i in range(1,6)}
print(dct)
print('-'*50)
dct={i:i**3 for i in range(1,1000)}
print(dct)
print('-'*50)
#dictionaries with condition
dct={i:i**2 for i in range(1,11) if i%2==0}
print(dct)

print('-'*50)

#convert lis to dict

lst=['Apple','Banana','Grapes']
data={item : len(item) for item in lst}
print(lst)
print(data)

lst=['Apple','Banana','Grapes']
data={item : len(item) for item in lst}
print(lst)
print(data)
dct3={len(item): item  for item in lst}
print(dct3)

print('-'*50)

#special keys with string
dct={'num_'+str(i):i for i in range(1,101)}
print(dct)
print('-'*50)
#shortlisting based on values
dct={'num_'+str(i):i for i in range(1,11) }
dct={k:v for k,v in dct.items() if v%3==0}
print(dct)

#making dictionary from two list
print('-'*50)
lst1=['a','b','c']
lst2=[1,2,3]
dict_12={lst2[i]:lst1[i] for i in range(len(lst1))}
print(dict_12)
#usng tuple as key
print('-'*50)
matrix=[[1,2,3],[4,5,6],[7,8,9]]
fdict={(i,j):matrix[i][j] for i in range(3) for j in range(3)}
print(fdict)

print('-'*50)
matrix=[[1,2,3],[4,5,6],[7,8,9]]
fdict={matrix[i][j]:(i,j) for i in range(3) for j in range(3)}
print(fdict)