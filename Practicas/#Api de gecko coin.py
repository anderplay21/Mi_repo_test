#Api de gecko coin
import pandas as pd
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='cop', days=30)
bitcoin_data

data = pd.DataFrame(bitcoin_data['prices'], columns=['timestamp', 'price'])
data['Date'] = pd.to_datetime(data['timestamp'], unit='ms')

print(data.head())

import matplotlib.pyplot as plt

candlestick_data = data.groupby(data.Date.dt.date).agg({'price': ['min', 'max', 'first', 'last']})


# Importamos la biblioteca necesaria
import plotly.graph_objects as go

# Supongamos que candlestick_data es un DataFrame previamente definido con datos válidos
# Asegúrate de que candlestick_data tenga las columnas y estructura necesarias:
# index, price['first'], price['max'], price['min'], price['last']

# Creación del gráfico de velas
fig = go.Figure(data=[go.Candlestick(
    x=candlestick_data.index,            # Eje X: índice del DataFrame (fechas)
    open=candlestick_data['price']['first'],  # Valores de apertura
    high=candlestick_data['price']['max'],    # Valores máximos
    low=candlestick_data['price']['min'],     # Valores mínimos
    close=candlestick_data['price']['last']   # Valores de cierre
)])

# Configuración del diseño del gráfico
fig.update_layout(
    xaxis_rangeslider_visible=False,     # Opcional: oculta el deslizador de rango
    xaxis_title='Date',                  # Título del eje X
    yaxis_title='Price (USD)',           # Título del eje Y
    title='Bitcoin Candlestick Chart 30 days' # Título del gráfico
)

# Mostrar el gráfico
fig.show()
