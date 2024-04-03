# Przygotuj program, który wyliczy i wyświetli podstawowe dane oraz wszystkie raty miesięczne kredytu
# na podstawie następujących danych:
#
# kwota kredytu
# liczba lat
# procent w skali roku
# typ raty (malejące/stałe)
# Obliczanie rat malejących - https://matematykafinansowa.pl/jak-wyliczyc-rate-malejaca-kredytu/
# Obliczanie rat stałych - http://matematykafinansowa.pl/jak-wyliczyc-rate-rowna-kredytu/
#
# Na początku program powinien poinformować o wprowadzonych parametrach i całkowitym koszcie kredytu
# (sumie odsetek ze wszystkich rat), a następnie wyświetlić Informacje o poszczególnych ratach zawierające
# następujące dane:
#
# numer kolejny raty
# część kapitałowa raty
# część odsetkowa raty
# wysokość raty
# kapitał pozostały do spłaty po opłaceniu raty.
# Poprawnie przygotowany program powinien pobrać od użytkownika wymagane wartości.
# Program powinien też odpowiednio informować użytkownika jeśli dla wprowadzonych wartości
# niemożliwe jest wygenerowanie listy rat (informując, która z wprowadzonych wartości jest problematyczna).

def kredyt(kwota_kredytu, liczba_lat, procent, typ_raty):



    return kwota_kredytu, liczba_lat, procent, typ_raty

wejscie1 = input("Podaj kwotę kredytu: ")
wejscie2 = input("Podaj liczbę lat: ")
wejscie3 = input("Podaj procent w skali roku: ")
wejscie4 = input("Podaj typ raty: ")

wynik = kredyt(wejscie1, wejscie2, wejscie3, wejscie4)

print(f"Poniżej podane są parametry, które zostały wprowadzone do systemu. Sprawdź czy są poprawne:"
      f" \n1. Kwota kredytu {wynik[0]} \n2. Liczba lat {wynik[1]} \n3. Procent w skali roku: {wynik[2]} \n4. Typ raty: {wynik[3]}")

#
##
###
##
#