class agent:
     def __init__(self,name,age):
         print('Welcome to the Game')
         self.name= name
         self.age= age 
         self.health=100
         self.alive=True
     
     def curr_health(self):
         print('Current Health of',self.name,'is',self.health)
     def punched(self):
         self.health -=10
         self.is_alive()
     def shot(self):
         self.health-=50
         self.is_alive()
     def is_alive(self):
         if self.health<=0:
             self.alive=False
         else:
             self.alive=True
     def info(self):
         print("Name    :",self.name)
         print('Age     :',self.age)
         print('Health  :',self.health)
         print('Alive   :',self.alive)

p1=agent('Rohan',25)
p1.curr_health()
p1.punched()
p1.shot()
p1.shot()
p1.shot()
p1.info()