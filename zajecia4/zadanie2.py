# Program powinien pozwolić użytkownikowi na grę w "Kamień, Papier i Nożyce"
# do momentu w którym użytkownik przerwie jego działanie. Implementacja powinna:
#
# przechowywać aktualny wynik oraz informować o nim po każdej rundzie
# pobrać od użytkownika jego wybór w postaci liter "K", "P" bądź "N"
# wykorzystując bibliotekę "random" losować wybór komputera w każdej rundzie

import random

def runda(wybor_gracza, wybor_komputera):
    if wybor_gracza == wybor_komputera:
        return "Remis"
    elif (wybor_gracza == "K" and wybor_komputera == "N") or \
         (wybor_gracza == "P" and wybor_komputera == "K") or \
         (wybor_gracza == "N" and wybor_komputera == "P"):
        return "Gracz wygrywa"
    else:
        return "Komputer wygrywa"

def get_wybor_komputera():
    return random.choice(["K", "P", "N"])

def wyswietl_wynik(wynik):
    print("Wynik:", wynik)

punktacja = {'gracz': 0, 'komputer': 0}

print("Witaj w grze w 'Kamień, Papier i Nożyce'")

while True:

    wybor = input("Jeśli chcesz grać dalej wybierz tak, w przeciwnym wypadku wybierz nie: ")

    if wybor == "tak":

        wybor_gracza = input("Wybierz Kamień (K), Papier (P) lub Nożyce (N): ")
        wybor_komputera = get_wybor_komputera()
        print("Komputer wybrał:", wybor_komputera)

        wynik = runda(wybor_gracza,wybor_komputera)
        wyswietl_wynik(wynik)

        if wynik == "Gracz wygrywa":
            punktacja['gracz'] += 1
        elif wynik == "Komputer wygrywa":
            punktacja['komputer'] += 1

        print(f"\nAktualna punktacja:\nGracz:", punktacja['gracz'], "\nKomputer:", punktacja['komputer'])

    elif wybor == "nie":
        print("\nDziękuje za grę, do zobaczenia!")
        break
    else:
        print("Musi wybrać tak lub nie.")
