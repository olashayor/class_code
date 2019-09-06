birth_year = input('Birth year: ')
print(type (birth_year))
age = 2019 - int(birth_year)
print(type (age))
print (age)

weight = input('Body weight in pounds: ')
weight_kg = int(weight) * 0.45
print(weight_kg)

course = "python's course' for beginners"
print(course)
print(course[-1])
print(course.upper())
print(course.lower())
print(course.find('p'))
print(course.replace ('beginners' , 'absolute beginners'))
print('beginners' in course)
print('absolute' in course)
print('Absolute' in course)

name = 'jennifer'
print(name [1:-1])

email = ('hi shayor, \n'
    'how are u doing?\n'
    'is being a while\n'
    'love u\n'
    'puku')
print("\n EMAIL \n", email)
