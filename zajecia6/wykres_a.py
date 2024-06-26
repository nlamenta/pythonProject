# W ramach utworzonej klasy przygotuj program, który na podstawie parametrów podanych przez użytkownika wyświetli na
# konsoli „wykres” wg wzoru podanego poniżej.
# Program odpytuje użytkownika o wartość dwóch parametrów odpowiadających za wysokość dwóch skrajnych słupków wykresu:
# 1. wysokość pierwszego słupka (a),
# 2. wysokość trzeciego słupka (c).
# Program wyświetla odpowiedni komunikat i kończy działanie jeśli podane parametry nie spełniają poniższych warunków:
# • wysokość dowolnego słupka musi być większa od 0 i mniejsza niż 20,
# • wysokości podanych słupków muszą być różne.
# Wysokość drugiego słupka (b) program wylicza jako średnią arytmetyczną dwóch podanych wartości (zaokrągloną do liczby
# całkowitej).
# Na koniec program wyświetla wykres wg. poniższego wzorca. Poniższe wzory wygenerowano dla różnych wartości parametrów a i c.

def wykres_a(wysokosc_a, wysokosc_c):

    wysokosc_b = (wysokosc_a + wysokosc_c) // 2

    wysokosci = [wysokosc_a, wysokosc_b, wysokosc_c]

    for wysokosc_i in wysokosci:

        print(" " * (max(wysokosci) + 1) + "|" )
        print(" " * (max(wysokosci) - wysokosc_i) + "+" + "-" * wysokosc_i + "+")
        print(" " * (max(wysokosci) - wysokosc_i) + "|" + " " * wysokosc_i + "|")
        print(" " * (max(wysokosci) - wysokosc_i) + "+" + "-" * wysokosc_i + "+")

    print(" " * (max(wysokosci) + 1) + "|")

while True:
    # pobranie wartości od usera
    try:
        wysokosc_a = int(input("Podaj wysokość: "))
        wysokosc_c = int(input("Podaj wysokość: "))
    except ValueError:
        print("Wysokość musi być liczbą całkowitą!")
        continue

    #sprawdzenie czy wartość jest dodatnia
    if not (0 <= wysokosc_a <= 20 and 0 <= wysokosc_c <= 20):
        print("Wysokość musi być z przedziału od 0 do 20!")
    else:
        if wysokosc_a == wysokosc_c:
            print("Musisz podać dwie różne wysokości!")
        else:
            wykres_a(wysokosc_a, wysokosc_c)
        break

