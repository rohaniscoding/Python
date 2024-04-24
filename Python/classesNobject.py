class person:
    name='Rohan'
    age= 22
    print('Hello')

p1=person()
print(p1.name)
print(p1.age)
print('-'*30)

p1.name='Ankur'
p1.age= 23
print(p1.name)
print(p1.age)
print('-'*30)

p2=person()
print(p2.name)
print(p2.age)
print('-'*30)

#MEthods

class Mathematics:
    name='Raghav'
    def greet(self):
        print('Hello')
        return 'Hi'
        # print(self.name)
    def factorial(self,n):
        s=1
        for i in range(1,n-1):
            s*=i
        return s
    def lst_multi(self,lst):
        s1=1
        for i in lst:
            s1*=i
        return s1
    def lst_dot(self,lst1,lst2):
        return [lst1[i]*lst2[i] for i in range(len(lst1))]
math=Mathematics()
print(math.greet())
print('-'*30)
print(math.factorial(5))
print('-'*30)
print(math.lst_multi([3,4,5]))
print('-'*30)
print(math.lst_dot([1,2,3,4],[2,3,4,5]))
print('-'*30)
