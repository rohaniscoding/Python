class person:
     def __init__(self,name,age):
         self.name= name
         self.age= age 
     
     def run(self):
         print(self.name)
         print('run!')
p1=person('Rohan',25)
p2=person('Ankur',30)
p3=person('Dhruv',20)
# print(p1.run())
print('_'*30)
p1.run()
p2.run()
p3.run()
print('-'*30)