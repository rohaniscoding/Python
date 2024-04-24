lst=[1,2,3,4,5,6]
print(lst)
lst=[i*2 for i in lst]
print(lst)
lst=[i*2 for i in lst]
print(lst)
print('-'*20)

#finding first 10 even number
print([i for i in range(21) if i%2==0])
print('-'*20)
#finding first 10 even number and Square it
print([i**2 for i in range(21) if i%2==0])