import pandas as pd

# Wczytaj dane z pliku CSV
df = pd.read_csv('movies.csv', sep=';', encoding="ISO-8859-1")
# Wyświetl pierwsze 3 wiersze tabeli
#print(df.head(3))

# Wyświetl statystyki opisowe dla kolumny "Popularity"
# df['Popularity'].describe()
# Wyświetl informacje o typach danych i ilości niepustych wartości w każdej kolumnie
#df.info()

# Obliczenie statystyk opisowych dla kolumny z długościami filmów
# df['Length'].describe()

# usunięcie drugiego wiersza

df.drop(index = 0, inplace = True)

# 1. Napisz metodę, który wczyta dane o filmach z pliku CSV do obiektu DataFrame Pandas,
# a następnie wyświetli wszystkie filmy z roku 2000.

df["Year"] = df["Year"].astype(int)
zadanie1 = df[df["Year"] == 200]


# 2. Napisz metodę, który wczyta dane o filmach z pliku CSV do obiektu DataFrame Pandas,
# obliczy i wyświetli średnią długość filmów wszystkich reżyserów.

df["Length"] = df["Length"].astype(float)
zadanie2 = df["Length"].mean()

# 3. Napisz metodę, który wczyta dane o filmach z pliku CSV do obiektu DataFrame Pandas,
# utworzy nowy plik CSV zawierający tylko kolumny z tytułem, reżyserem i popularnością dla każdego
# filmu oraz zapisze go pod nową nazwą.

zadanie3 = df[["Title", "Director", "Popularity"]].to_csv("3-kolumny.csv", index = False)

# 4. Napisz metodę, który wczyta dane o filmach z pliku CSV do obiektu DataFrame Pandas,
# obliczy i wyświetli procentowy udział filmów z nagrodami w stosunku do całkowitej liczby filmów.

nagrody = df[df["Awards"] == "Yes"]["Awards"].count()
calosc = df["Awards"].count()

zadanie4 = round((nagrody / calosc) * 100,2)

# 5. Napisz metodę, który wczyta dane o filmach z pliku CSV do obiektu DataFrame Pandas,
# a następnie wyświetli wszystkie filmy z reżyserem o nazwisku "Kubrick".

zadanie5 = df[df["Director"] == "Kubrick, Stanley"]["Title"]

# 6. Napisz metodę, który wczyta dane o filmach z pliku CSV do obiektu DataFrame Pandas,
# obliczy i wyświetli sumę popularności filmów z gatunkiem "comedy"

zadanie6 = df[df["Subject"] == "Comedy"]["Popularity"].sum()
