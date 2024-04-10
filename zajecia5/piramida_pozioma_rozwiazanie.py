#funkcja odpowiedzialna za generowanie piramidy poziomej
def generate_horizontal_pyramid(height):
    #generowanie górnej części
   for i in range(1, height + 1):
       print("#" * i)
    #generowanie dolnej części
    for i in range(height -1, 0, -1):
        print("#" * i)
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
        generate_horizontal_pyramid(height)
        break