#funkcje, które używamy potem w następnej funkcji
def add(a, b):
    result = a + b
    return result #tabulator = 4 spacje

def sub(a,b):
    return a - b

def mult(a,b):
    return a * b

def div(a,b):
    if b != 0:
        return a/b
    else:
        return "Cannot divide by zero!"

# while będzie wykonywana tak długo jak podany warunek jest prawdziwy

while True:
    print("Welcome to the calculator! Choose operation:")
    print("1. Add")
    print("2. Sub")
    print("3. Mul")
    print("4. Div")
    print("To exit, type 'end'")

    operation = input("Choose option: ") #input

    if operation == "end":  #zakonczenie operacji
        print('\ngoodbye!')
        break

    if operation in set("1234"):  #jako string
        print("\ngreat!")
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
        if operation == "1":
            print(f"Add result: {add(number1,number2)}")
        elif operation == "2":
            print(f"Sub result: {sub(number1, number2)}")
        elif operation == "3":
            print(f"Mul result: {mult(number1, number2)}")
        elif operation == "4":
            print(f"Div result: {div(number1, number2)}")
    else:
        print("\nInvalid option! PLease choose again")