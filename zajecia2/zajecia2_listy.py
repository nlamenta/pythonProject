zajecia = ["bazy danych", "programowanie", "python"]
print(zajecia) #wyświetlenie całej listy

print(zajecia[0]) #wyświetlamy po indeksie; w pythonie zaczynamy od 0
print(zajecia[0].title())

print(f"nie mogę się doczekać {zajecia[0]}")

print(zajecia[2])
print(zajecia[-1]) #ta i poprzednia linijka jest tym samym

print(zajecia)
zajecia[0] = "cyberbezpieczeństwo"
print(zajecia)  #zmiana w liście

zajecia.append("mikroekonomia")    #dodajemy element do listy; domyślnie idzie na koniec
print(zajecia)


zajecia.insert(0,"bazy danych")   #dodajemy element do listy; teraz wybieramy, na które miejsce ma wskoczyć
print(zajecia)

del zajecia[-1] #usuwanie elementu z listy po indeksie
print(zajecia)

print(f"zaliczono na 5 przedmiot: {zajecia.pop(-1)}") #co znaczy f przed cudzysłowiem
print(zajecia)

zajecia.insert(1, "programowanie")

zajecia.remove('programowanie') #usuwamy po nazwie; metoda remove usuwa pierwsze wystąpienie i usuwa, każde kolejne
print(zajecia)

## sortowanie
print(zajecia)
print(sorted(zajecia)) #sortowanie tymczasowe
print(zajecia)

zajecia.sort() #sortuje na stałe; alfabetycznie
print(zajecia)

zajecia.sort(reverse = True) #sortuje na stałe; odwrotnie do alfabetycznego
print(zajecia)

zajecia.reverse() #odwrócenie listy
print(zajecia)

print(len(zajecia))  #liczba elementów w liście

for przedmiot in zajecia:
    print("Lubię przedmiot " + przedmiot) #funkcja
