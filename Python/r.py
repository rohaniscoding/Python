my_dict = {'name':'Rose','age':24, 'gender':'Female'}
for key in my_dict:
    print(key, end=' ')
print('\n')
# Iterating through values
for value in my_dict.values():
    print(value, end=' ')
print('\n')
# Iterating through key-value pairs
for key, value in my_dict.items():
    print(key, value, end = ' ')
print('\n')
print(my_dict.items(),end=' ')