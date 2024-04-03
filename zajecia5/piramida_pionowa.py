# 1. Zdefiniuj zmienną całkowitoliczbową wysokosc i ustaw jej wartość np. na 7
# 2. Zdefiniuj zmienną całkowitoliczbową y i ustaw jej wartość na wysokosc - 1
# 3. Jeśli y jest większy lub równy 0 to przejdź do kroku 4, w przeciwnym przypadku zakończ działanie programu
# 4. Zdefiniuj zmienną całkowitoliczbową x
# 5. Ustaw wartość x na 1
# 6. Jeśli x < ( wysokosc * 2) przejdź do kroku 7, w przeciwnym razie przejdź do kroku 9
# 7. Jeśli x > y oraz x < ( wysokosc * 2 - y ) to wypisz na ekranie znak "#", w przeciwnym przypadku
# wypisz na ekranie znak " "
# 8. Zwiększ x o 1 i przejdź do kroku 6
# 9. Wypisz na ekranie znak końca linii.
# 10. Zmniejsz y o 1 i przejdź do kroku 3

def piramida_pionowa(wysokosc):
    y = wysokosc - 1

    while y >= 0:
        x = 1
        while x < wysokosc * 2:
            if y < x < wysokosc * 2 - y:
                print('#', end='')
            else:
                print(' ', end='')
            x += 1
        print("")
        y -= 1


piramida_pionowa(7)
