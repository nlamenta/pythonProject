# W ramach utworzonej klasy przygotuj program, który na podstawie parametrów podanych przez
# użytkownika wyświetli na konsoli „wykres” wg wzoru podanego poniżej.
# Program odpytuje użytkownika o wartość trzech parametrów odpowiadających za wysokość dwóch
# pierwszych słupków wykresu:
# 1. wysokość pierwszego słupka (a),
# 2. wysokość drugiego słupka (b).
# Program wyświetla odpowiedni komunikat i kończy działanie jeśli podane parametry nie spełniają
# poniższych warunków:
# • wysokość dowolnego słupka musi być większa lub równa 0 i mniejsza niż 9,
# • wysokości podanych słupków muszą być różne.
# Wysokość trzeciego słupka (c) program wylicza jako wartość bezwzględną różnicy podanych wysokości.
# Na koniec program wyświetla wykres wg. poniższego wzorca. Poniższe wzory wygenerowano dla
# różnych wartości parametrów a i b.

def wykres_a(wysokosc_a, wysokosc_b):

    wysokosc_c = abs(wysokosc_a - wysokosc_b)
    wysokosci = [wysokosc_a, wysokosc_b, wysokosc_c]
    wysokosci_max = max(wysokosc_a, wysokosc_b, wysokosc_c)
    wysokosci_min = min(wysokosc_a, wysokosc_b, wysokosc_c)
    wysokosc_srednia = wysokosci_max - wysokosci_min

    print( "-" * 2 + "+-+--" * 3)

    if wysokosc_a == wysokosci_min and wysokosc_b != wysokosc_c:

        for i in range(wysokosc_a - 1):
            print(" " * 2 + "| |  " * 3)

        print(" " * 2 + "+ +  " + "| |  " * 2)

        if wysokosc_c == wysokosc_srednia:
            for i in range(wysokosc_c - wysokosc_a - 1):
                print(" " * 7 + "| |  " * 2)

            print(" " * 7 + "+ +  " + "| |  ")

            for i in range(wysokosc_b - wysokosc_c - 1):
                print(" " * 12 + "| |")
            print(" " * 12 + "+ +")
    elif wysokosc_a == wysokosci_min and wysokosc_b == wysokosc_c:
        for i in range(wysokosc_a - 1):
            print(" " * 2 + "| |  " * 3)

        print(" " * 2 + "+ +  " + "| |  " * 2)

        for i in range(wysokosc_c - wysokosc_a - 2):
            print(" " * 7 + "| |  " * 2)

        print(" " * 7 + "+ +  " + "+ +  ")

    if wysokosc_b == wysokosci_min and wysokosc_c != wysokosc_a:

        for i in range(wysokosc_b - 1):
            print(" " * 2 + "| |  " * 3)

        print(" " * 2 + "| |" + " " * 2 + "+ +  " + "| |  ")

        if wysokosc_c == wysokosc_srednia:
            for i in range(wysokosc_c - wysokosc_b - 1):
                print(" " * 2 + "| |" + " " * 7 + "| |")

            print("  " + "| |" + " " * 7 + "+ +")

            for i in range(wysokosc_a - wysokosc_c - 1):
                print(" " * 2 + "| |")
            print(" " * 2 + "+ +")

    elif wysokosc_b == wysokosci_min and wysokosc_a == wysokosc_c:
        for i in range(wysokosc_b - 1):
            print(" " * 2 + "| |  " * 3)

        print(" " * 2 + "| |" + " " * 2 + "+ +  " + "| |  ")

        for i in range(wysokosc_c - wysokosc_b - 2):
            print(" " * 2 + "| |" + " " * 7 + "| |")

        print("  " + "+ +" + " " * 7 + "+ +")

    if wysokosc_c == wysokosci_min:

        for i in range(wysokosc_c - 1):
            print(" " * 2 + "| |  " * 3)

        print(" " * 2 + "| |" + " " * 2 + "| |  " + "+ +  ")

        if wysokosc_b == wysokosc_srednia:
            for i in range(wysokosc_b - wysokosc_c - 1):
                print(" " * 2 + "| |  " * 2)

            print("  " + "| |  " + "+ +" )

            for i in range(wysokosc_a - wysokosc_b - 1):
                print(" " * 2 + "| |")
            print(" " * 2 + "+ +")

        if wysokosc_a == wysokosc_srednia:
            for i in range(wysokosc_a - wysokosc_c - 1):
                print(" " * 2 + "| |  " * 2)

            print("  " + "+ +  " + "| |" )

            for i in range(wysokosc_b - wysokosc_a - 1):
                print(" " * 7 + "| |")
            print(" " * 7 + "+ +")



while True:
    # pobranie wartości od usera
    try:
        wysokosc_a = int(input("Podaj wysokość: "))
        wysokosc_b = int(input("Podaj wysokość: "))
    except ValueError:
        print("Wysokość musi być liczbą całkowitą!")
        continue

    #sprawdzenie czy wartość jest dodatnia
    if not (0 <= wysokosc_a <= 9 and 0 <= wysokosc_b <= 9):
        print("Wysokość musi być z przedziału od 0 do 9!")
    else:
        if wysokosc_a == wysokosc_b:
            print("Musisz podać dwie różne wysokości!")
        else:
            wykres_a(wysokosc_a, wysokosc_b)
        break


