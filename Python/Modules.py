from support import greet, subm , arth , sq , cube, finals
# from support import *
lst=[1,2,3,4,5]
print(greet('Rohan'))
print(subm(10,5))
print(arth(10,5))
# print(sq(lst)) return object
# print(cube(lst))
sq_gen = sq(lst)
cube_gen = cube(lst)

# Convert generator objects to lists
sq_list = list(sq_gen)
cube_list = list(cube_gen)

print(sq_list)
print(cube_list)
