# funkcja odpowiedzialna za generowanie pionowej piramidy

def generate_vertical_pyramid(height):
    # iteracja od góry do dołu piramidy
    for y in range (height - 1, -1, -1): # start, stop, krok
        # iteracja po każdej lini
        for x in range(1, height * 2):
            # jeśli wartość w zakresie wypisz #
            if x > y and x < (height * 2 - y):
                print("#", end= "")
            # inaczej spacja
            else:
                print(" ", end= "")
        # zakończ linie
        print()

# print(generate_vertical_pyramid(10))

while True:
    # pobranie wartości od usera
    try:
        height = int(input("Podaj wysokość piramidy: "))
    except ValueError:
        print("Wysokość piramidy musi być liczbą całkowitą!")
        continue
    #sprawdzenie czy wartość jest dodatnia
    if height <= 0:
        print("Wysokość musi być liczbą dodatnią")
    else:
        generate_vertical_pyramid(height)
        break