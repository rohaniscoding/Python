#string
#Concatenation
print('Rohan '+' Kukreti')
print('-------------')

#string replicate
print('r'*3)
print('rohan'*3)
print('-'*10)

#string Length
print(len('Rohankukreti'))
print('-'*10)

#string Slicing/Indexing
print('Rohan Kukreti')
print('Rohan Kukreti'[5])
print('Rohan Kukreti'[4])
print('Rohan Kukreti'[-1])
print('Rohan Kukreti'[-6])
print('Rohan Kukreti'[0:6])
print('Rohan Kukreti'[6:13])
print(('Rohan Kukreti')[2:5])
print('Rohan Kukreti'[:7])
print('-'*12)
#string case conversion
print('Rohan KUkreti'.lower())
print('Rohan KUkreti'.upper())
print('-'*12)

#sting Stripping
print('     Rohan Kukreti     '.strip()) #removes the space from the beggining and the last
print('-'*12)

#string Replaced
print('Rohan kukreti'.replace('a','7'))
print('-'*12)

#string count
print('ROHAN KUKRETI'.count('a'))
print('ROHaN KUKRETI'.count('a'))
print('-'*12)
#string Find
print('Rohan KUkreti'.find('a'))
print('Rohan KUKRETI'.find('han'))

#string Check
print('Rohan'.isalpha())
print('123'.isdigit())
print('rohan'.islower())
print('ROHAN'.isupper())
print('-'*12)


#string Captiliazed
print('rohan'.capitalize())
print('rohan'.title())
print('-'*12)

#check for start and end
print('Rohan kukreti'.startswith('Roh'))
print('Rohan kukreti'.endswith('reti'))
print('-'*12)
#
print('rohan'.center(20,"-"))
print('RohanKurketi'.ljust(20,"*"))
print('RohanKurketi'.rjust(20,"*"))
print('-'*12)