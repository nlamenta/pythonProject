import requests # biblioteka ta służy do wykonywania zapytań (pobierania danych z internetu)
import json # biblioteka ta przetwarza dane w formacie json, tak aby można je było dalej obrabiać w kodzie (np. automatycznie mapuje tablice danych)
import pandas as pd # ta biblioteka z kolei pozwala na przetwarzanie zbiorów danych i przygotowywanie obiektów, które poźniej będą wykorzystywane przy rysowaniu wykresów
import mplfinance as mpl # biblioteka ta jest rozszerzoną biblioteką do rysowania wykresów, zawiera dodatkowe metody do rysowania wykresów finansowych

url = 'https://www.mexc.com/open/api/v2/market/kline?symbol=SRT_USDT&interval=60m&limit=10' # tutaj należy umieścić adres url który zwraca jsona z danymi na temat świeczek (z poprzedniego zadania z Postmanem)
response = requests.get(url) # wywołanie to pobiera zasób znajdujący się pod danym adresem url
responseBody = response.text # obiekt response zawiera atrybut "text", z naszymi danymi (całe response zawiera jeszcze dodatkowo metadane zapytania, które nie są nam potrzebne)
responseBodyJson = json.loads(responseBody) # przetwarzamy tekst w formacie json

candlesData = responseBodyJson["data"] # wyciągamy jedynie tablicę wartości do której odwołamy się po kluczu "data".

keys = ['time', 'open', 'close', 'high', 'low']


formattedCandlesData = []
for value in candlesData:
    row = {}
    for i, key in enumerate(keys):
        if key != 'time':
            row[key] = float(value[i])
        else:
            row[key] = value[i]
    formattedCandlesData.append(row)

df = pd.json_normalize(formattedCandlesData) # przetwarzamy dane w formacie json
df.time = pd.to_datetime(df.time, unit='s') # ponieważ oczekiwany format daty w kolumnie "time" jest inny niż oczekiwany przez bibliotekę to musimy go skonwertować
df = df.set_index("time") # ustawiamy index naszych danych na kolumnę "time"

print(df.columns) # wyświetlanie tego atrybutu zwróci nam listę kolumn - "Index(['open', 'close', 'high', 'low'], dtype='object')"
print(df.head()) # funkcja head wywołana na obiekcie df pozwoli nam wyświetlić podgląd naszych danych wraz z nagłówkami

mpl.plot(
    df, # przekazujemy obiekt z danymi
    type="candle", # określamy typ wykresu
    title="Candle chart", # nadajemy tytuł naszego wykresu
    style="yahoo", # wersja kolorystyczna naszego wykresu - inne to np. binance, blueskies, brasil, charles, checkers, classic, default, mike, nightclouds, sas, starsandstripes
    mav=(3, 6, 9) # atrybut który włączy automatyczne obliczanie oraz rysowanie średni kroczących
)