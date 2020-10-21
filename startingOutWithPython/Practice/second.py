#Dictionaries
Courses={
    'Nicholas': 'Applied Computer Science',
    'Tembe': 'Medicine',
    'Tiff': 'Psychology',
    'Nick': 'Computers',
    'Davi': 'Coding',
    'Jenny': 'Nursing'
}
for name, course in Courses.items():
    print(f"{name.capitalize()}'s course of study is {course.capitalize()}. ")
for name in Courses.keys():
    print(name.capitalize())