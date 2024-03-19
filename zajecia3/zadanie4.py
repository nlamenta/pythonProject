# input
tekst = input("Wprowadź tekst: ")

# zmienne
liczba_liter = 0
liczba_interpunkcji = 0
liczba_spacji = 0
znaki_interpunkcyjne = set(".;,:-?!()""")

# sprawdzamy liczbę liter, znaków interpunkcyjnych i spacji
for znak in tekst:
    if znak.isalpha():
        liczba_liter += 1
    elif znak in znaki_interpunkcyjne:
        liczba_interpunkcji += 1
    elif znak.isspace():
        liczba_spacji += 1

# zliczanie wyrazów
liczba_wyrazow = len(tekst.split())

print("Liczba liter:", liczba_liter)
print("Liczba znaków interpunkcyjnych:", liczba_interpunkcji)
print("Liczba spacji:", liczba_spacji)
print("Liczba wyrazów:", liczba_wyrazow)
