import yfinance as yf
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tickers = ["SPY", "EWU", "AGG", "DBC"]

data = yf.download(tickers, period="3y")

close_prices = data["Close"]
returns = close_prices.pct_change().dropna()

correlation = returns.corr()
volatility = returns.std()
avg_return = returns.mean()

print(correlation)
print(volatility)
print(avg_return)

sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("ETF Correlation Heatmap")
plt.show()