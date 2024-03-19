#listy
numbers = [1,2,3,4,5]
numbers_in_range = list(range(1,6))

print(numbers)
print(numbers_in_range)

for value in numbers:
    print(value)

for value in range(1,11):
    print(value)

squares = []

for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

even_numbers = list(range(2,11,2)) #co ile lista
print(even_numbers)

for square in squares:
    print(square)

for value in range(0, len(squares)): #zbiór otwarty po prawej stronie
    print(squares[value])


#wycianie z list

students = ['adam', 'natalia', 'ola', 'filip']
print(students[0:2]) #wycienk 2 pierwszych wartości
print(students[:2]) #wycienek 2 pierwszych wartości
print(students[1:3]) #wycienk 2 wartości - 2 i 3
print(students[2:4]) #wycinek 2 ostatnich
print(students[2:]) #wycinek 2 ostatnich
print(students[-2:]) #wycinek 2 ostatnich

another_students = students #kopiowanie a przypisywanie listy

print(id(students))
print(id(another_students))

cars = ['audi', 'bmw', 'toyota', 'subaru']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    elif car == 'audi':
        print(car)
    else:
        print(car.title())


for car in cars:
    is_bmw = car == 'bmw'
    is_skoda = car == ('skoda')
    print(f"is_bmw: {is_bmw}")
    print(f"is_skoda: {is_skoda}")
    if is_bmw :
        print(car.upper())
    elif is_skoda:
        print(car)