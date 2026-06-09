# Portfolio Analysis Tool (Python)

## Overview
This project is a Python-based portfolio analysis tool that uses real ETF market data to evaluate risk, return, and diversification across asset classes. It is designed to replicate basic workflows used in investment risk analysis.

---

## Objective
To understand how different asset classes behave relative to each other and how diversification reduces portfolio risk.

---

## Methodology
- Collected historical price data for ETFs using `yfinance`
- Calculated daily percentage returns
- Measured:
  - Volatility (risk)
  - Average returns
  - Correlation between assets
- Visualised relationships using a correlation heatmap

---

## ETFs Analysed

| ETF | Asset Class |
|-----|-------------|
| SPY | US Equities |
| EWU | UK Equities |
| AGG | Government Bonds |
| DBC | Commodities |

---

## Key Insights
- Equities (SPY, EWU) show relatively high correlation, meaning they tend to move together.
- Bonds (AGG) show lower correlation with equities, providing diversification benefits.
- Commodities (DBC) behave differently from equities, adding diversification.
- Combining multiple asset classes reduces overall portfolio volatility compared to holding a single asset.

---

## Output
- Correlation matrix
- Volatility estimates
- Average daily returns
- Heatmap visualization of asset relationships

---

## Tools Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- yfinance
