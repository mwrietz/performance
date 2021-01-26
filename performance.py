#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot as plt
import yfinance as yf
from tqdm import tqdm

#symbols = ['^DJI', '^GSPC' ,'^IXIC', 'AAPL', 'ARKG', 'VOO']
dates = '10y' # 'ytd', '1d', 1y', '10y'

with open('tickersymbols.txt', 'r') as tickers:
    symbols = tickers.read().split('\n')
    symbols = list(filter(None, symbols))

print()
print(f'plotting {dates} performance of {symbols}')
print()

tqdmsymbols = tqdm(symbols)

dfs = []
for symbol in tqdmsymbols:
    ticker = yf.Ticker(symbol) 
    data = ticker.history(period=dates)
    price = data.iloc[0,:]['Close']
    no_shares = 10000.0/price
    data['Performance'] = no_shares*data['Close']
    dfs.append(data)
    tqdmsymbols.set_description('Processing %s' % symbol)

ax = plt.gca()
for df in dfs:
    df.plot(y='Performance', figsize=(20,14), ax=ax)
ax.legend(symbols)
ax.set_title(dates)
ax.grid()
plt.show()

