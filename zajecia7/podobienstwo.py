import requests
import json
import pandas as pd
import mplfinance as mpl

# Pobierz dane dotyczące świec japońskich
url = 'https://www.mexc.com/open/api/v2/market/kline?symbol=BTC_USDT&interval=1m&limit=1000'
response = requests.get(url)
responseBody = response.text
responseBodyJson = json.loads(responseBody)

# Wyodrębnij dane dotyczące świec
candlesData = responseBodyJson["data"]

# Zdefiniuj listę kluczy
keys = ['time', 'open', 'close', 'high', 'low']

# Zdefiniuj listę, która będzie zawierać dane w odpowiednim formacie
formattedCandlesData = []

# Przekształć dane do odpowiedniego formatu
for value in candlesData:
    row = {}
    for i, key in enumerate(keys):
        if key != 'time':
            row[key] = float(value[i])
        else:
            row[key] = value[i]
    formattedCandlesData.append(row)

# Stwórz ramkę danych z danymi o świecach
df = pd.json_normalize(formattedCandlesData)

# Konwertuj czas do formatu datetime
df.time = pd.to_datetime(df.time, unit='s')

# Ustaw indeks na czas
df = df.set_index("time")

# Znajdź dopasowanie struktury ostatnich 10 świec
pattern = df.tail(10)

# Znajdź indeks, na którym zaczyna się dopasowanie
start_index = None
for i in range(len(df) - 10):
    if df.iloc[i:i+10].equals(pattern):
        start_index = i
        break

# Jeśli znaleziono dopasowanie, wyświetl wykres
if start_index is not None:
    # Wybierz 10 ostatnich świec oraz dopasowanie
    matched_candles = df.iloc[start_index:start_index+10]

    # Wygeneruj wykres
    mpl.plot(
        matched_candles,
        type="candle",
        title="Matching Candlesticks",
        style="yahoo",
        mav=(3, 6, 9)
    )
else:
    print("Nie znaleziono dopasowania.")

# Wyświetl wykres
mpl.show()
