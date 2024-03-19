lista = [8,3,7,5,1]

def sum_czy_iloczyn (liczba):
    czy_rowna_sie = False
    #liczba = int(liczba)
    for i in range(len(lista)): #ta pętla iteruje przez indeksy od 0 do długość liczty -1; i odpowiada indeksowi
        for j in range(i+1,len(lista)): #jest i oraz j=i+1 dodatkowo z każdą iteracją j się zwiększa
            suma = lista[i] + lista[j]
            iloczyn = lista[i] * lista[j]
            if liczba == suma:
                print(f"Suma {lista[i]} i {lista[j]} wynosi {liczba}.")
                czy_rowna_sie = True
            if liczba == iloczyn:
                print(f"Iloczyn {lista[i]} i {lista[j]} wynosi {liczba}")
                czy_rowna_sie = True
    if not czy_rowna_sie:
        print(f"Liczba {liczba} nie jest ani sumą, ani iloczyne żadnej z liczb w liście")

# użytkownik podaje liczbę
liczba = int(input("Podaj liczba:"))

#sprawdzamy czy daje iloczyn albo sumę
sum_czy_iloczyn(liczba)