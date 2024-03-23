# Przygotuj listę składającą się z cyfr Twojego NIU, bez powtórzeń (np. dla NIU - 87655 powinna to być lista - [8,7,6,5]).
#
# Następnie przygotuj dwie metody przyjmującą jako argument przygotowaną listę. Obie metody wykorzystując sortowanie bąbelkowe,
# powinny ją posortować - pierwsza malejąco, druga rosnąco, a następnie zwrócić posortowane listy. Na koniec działania programu wyświetl obie listy.
#
# Algorytm zaimplementowany w ramach sortowania bąbelkowego powinien:
#
# przechodzić po poszczególnych elementach listy
# sprawdzać czy następny element jest mniejszy/większy i jeśli tak to zastępować je miejscami
# powtarzać czynność dla każdego kolejnego elementu listy
# po każdej iteracji (przejściu po wszystkich elementach z listy) największa liczba powinna znaleźć się na początku/końcu (wypłynąć niczym bąbelek)
# algorytm powinien przerwać działanie jeśli ostatnia iteracja nie zamieniła miejscami żadnych elementów



def sortowanie_malejaco():
    lista = [8, 3, 7, 5, 1]
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[j] > lista[i]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista

posortowana_malejaco_lista = sortowanie_malejaco()
print(posortowana_malejaco_lista)

def sortowanie_rosnaco():
    lista = [8, 3, 7, 5, 1]
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[j] < lista[i]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista


posortowana_rosnaco_lista = sortowanie_rosnaco()
print(posortowana_rosnaco_lista)