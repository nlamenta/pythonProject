lista = [8, 3, 7, 5, 1]

def sum_czy_iloczyn(liczba):
    liczba = int(liczba)  # Konwertujesz wprowadzoną liczbę na typ int
    znaleziono = False  # Zmienna, która będzie informować, czy znaleziono sumę lub iloczyn
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            suma = lista[i] + lista[j]
            iloczyn = lista[i] * lista[j]
            if liczba == suma:
                print(f"Suma {lista[i]} i {lista[j]} wynosi {liczba}.")
                znaleziono = True
            if liczba == iloczyn:
                print(f"Iloczyn {lista[i]} i {lista[j]} wynosi {liczba}")
                znaleziono = True
    if not znaleziono:  # Jeśli nie znaleziono ani sumy ani iloczynu
        print(f"Liczba {liczba} nie jest ani sumą, ani iloczynem żadnej z liczb w liście")

# użytkownik podaje liczbę
liczba = input("Podaj liczba:")

# sprawdzamy czy daje iloczyn albo sumę
sum_czy_iloczyn(liczba)
