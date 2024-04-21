import pylab # zaimportowanie biblioteki zawierającej metody potrzebne do utworzenia wykresu

x = [1, 2, 3] # zdefiniowanie tablicy wartości na osi X
y = [3, 2, 1] # zdefiniowanie tablicy wartości na osi Y
pylab.plot(x, y) # metoda przyjmująca tablicę wartości x oraz y, która przygotuje wykres
pylab.title('Super wykres') # metoda przyjmująca string, który będzie tytułem wykresu
pylab.grid(True) # metoda przyjmująca wartość boolean, definiująca czy ma zostać wyświetlona siatka pomocnicza
pylab.show() # metoda wyświetlającą przygotowany wykres
