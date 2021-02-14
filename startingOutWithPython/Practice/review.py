import random
#type conversion
x=1 #float
y=2.6 #float
z=1j #complex

#converting from int to float
a=float(x)
#converting from int to complex
b=complex(x)
#converting from float to int
c=int(y)

print(a)
print(b)
print(c)

print(random.randrange(1, 10))

#Strings
name='Nicholas'
print(name[1])
#loopinf through strings
for char in name:
    print(char)
#Lenth of the string
print(len(name))
#Check if a phrase or character is present in a string
print('free' not in name)
#slicing strings
print(name[2:5])
#string methods
print(name.upper())
print(name.lower())
print(name.replace('N', 'M'))
