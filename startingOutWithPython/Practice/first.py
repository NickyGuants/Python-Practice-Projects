#lists
names=['nick', 'marya', 'tembe', 'davi', 'hose']
names.append('tiff')
for i in names:
    greeting=f"Hello {i.capitalize()}."
    #print(greeting)

guests=['Obama', 'Bruno', 'Lovato', 'Demi']
for guest in guests:
    message=f"{guest.capitalize()} welcome to dinner."
    #print(message)

numbers=list(range(1, 10))
#print(numbers)

squares=[]
for value in range(1, 20):
    square=value**2
    squares.append(square)
#print(squares)
#print(min(squares))
#print(max(squares))
#print(sum(squares))
squares=[value**2 for value in range(1, 5)]
#print(squares)

numbers_odd= list(range(3, 30, 3))
#print(numbers_odd)
for value in range(1, 10):
    values=value**3
    #print(values)

values=[value**3 for value in range(1, 10) ] 
print(values)