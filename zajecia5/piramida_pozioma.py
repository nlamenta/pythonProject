# Zadanie polega na opracowaniu algorytmu oraz implementacji kodu generującą piramidę poziomą w konsoli.
#
# W przypadku tego zadania przed przejściem do implementacji konieczne jest opracowanie algorytmu
# (przemyślenie jak ma zachowywać się nasz program), który zapewni poprawne działanie.
#
# Poprawnie przygotowany program powinien pobrać od użytkownika wartość określającą wysokość i
# na jej podstawie wygenerować piramidę. Program powinien też odpowiednio informować użytkownika
# jeśli dla wprowadzonej wartości niemożliwe jest wygenerowanie piramidy.
#

def piramida_pozioma(wysokosc):
    for i in range(1, wysokosc + 1):
        print('#' * i)
    for i in range(wysokosc - 1, 0, -1):
        print('#' * i)

piramida_pozioma(3)

