# #loops
#  n=int(input('Enter the number'))
# for i in range(1,101):
#     print(i,'*',n,'=',i*n)

# for i in range(1,11,2):
#     print(i)

# for i in range (2,21,2):
#     print(i)

# n=int(input('Enter the number'))
# for i in range (n,(n*10)+1,n):
#      print(i)

# Nested for loop
# for i in range(1,7,1): #rows
#     for j in range(1,7,1):
#       print(i,j)
#       print("\n")

#sum=n and proability for 2 dices
for n in range(1,13):
     num=0
     for i in range(1,7,1): #rows
          for j in range(1,7,1):
               if(i+j==n):
                num+=1
     print(n,'=',round((num/36)*100,2))

#sum=n and proability for 3 dices
for n in range(1,13):
     num=0
     for i in range(1,7,1): #rows
          for j in range(1,7,1):
               for k in range(1,7,1):
                    if(i+j==n):
                     num+=1
     print(n,'=',round((num/36)*100,2))

