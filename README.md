# Portfolio Analysis Tool (Python)

# Overview
This project is a Python-based portfolio analysis tool that uses real ETF market data to evaluate risk, return, and diversification across asset classes. It is designed to replicate basic workflows used in investment risk analysis.

# Objective
To understand how different asset classes behave relative to each other and how diversification reduces portfolio risk.

# Methodology
Collected historical price data for ETFs using yfinance
Calculated daily percentage returns
Measured: 
 Volatility (risk)
 Average returns
 Correlation between assets
Visualised relationships using a correlation heatmap

# Features
- Downloads real ETF price data using yfinance
- Calculates daily returns
- Computes volatility (risk)
- Computes average returns
- Generates correlation matrix
- Visualises correlations using a heatmap

# ETFs Used
- SPY (US Equities)
- EWU (UK Equities)
- AGG (Bonds)
- DBC (Commodities)

# Key Insights
Equities (SPY, EWU) show relatively high correlation, meaning they tend to move together.
Bonds (AGG) show lower correlation with equities, providing diversification benefits.
Commodities (DBC) behave differently from equities, acting as an additional diversification component.
Overall, combining asset classes reduces portfolio volatility compared to holding a single asset type.

# Output
Correlation matrix
Volatility estimates
Average daily returns
Heatmap visualization of asset relationships

# Tools Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- yfinance
