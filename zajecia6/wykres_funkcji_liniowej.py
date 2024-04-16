# import numpy as np
# import matplotlib as mpl
# import pylab as pl
#
# x = [1, 3] # zdefiniowanie tablicy wartości na osi X
# y = [3, 1] # zdefiniowanie tablicy wartości na osi Y
# pl.plot(x, y) # metoda przyjmująca tablicę wartości x oraz y, która przygotuje wykres
# pl.title('Super wykres') # metoda przyjmująca string, który będzie tytułem wykresu
# pl.grid(True) # metoda przyjmująca wartość boolean, definiująca czy ma zostać wyświetlona siatka pomocnicza
# pl.show() # metoda wyświetlającą przygotowany wykres

import numpy as np
import matplotlib.pyplot as plt

def rysuj_wykres(a, b, zakres, tytul, siatka=False):
    x = np.linspace(zakres[0], zakres[1], 100)
    y = a * x + b

    # Tworzenie wykresu
    plt.plot(x, y)
    plt.title(tytul)
    plt.grid(True)
    plt.show()

# Pobranie danych od użytkownika
tytul = input("Podaj tytuł wykresu: ")
a = float(input("Podaj parametr a: "))
b = float(input("Podaj parametr b: "))
zakres = tuple(map(float, input("Podaj zakres wykresu (oddzielone przecinkiem): ").split(',')))
siatka = input("Czy wyświetlić siatkę pomocniczą? (tak/nie): ").lower() == 'tak'

# Wyświetlenie wykresu
rysuj_wykres(a, b, zakres, tytul, siatka)