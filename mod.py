import numpy as np
import pandas as pd
import yfinance as yf

#Assumption: There are 250 working days in a year

def stock_return_risk(ticker):
  df = yf.download(ticker, period="10y")
  df['daily_return'] = (df['Adj Close'] / df['Adj Close'].shift(1)) - 1
  average_annual_return = df['daily_return'].mean() * 252
  annual_volatility = df['daily_return'].std() * (250**0.5)
  return float(average_annual_return), float(annual_volatility)


def portfolio_return(securities, weights):
  df = pd.DataFrame()
  for ticker in securities:
    df[ticker] = yf.download(ticker, period='10y')['Adj Close']
  daily_returns = (df / df.shift(1)) - 1
  annual_returns = daily_returns.mean() * 250
  portfolio_annual_return = np.dot(annual_returns, weights)
  return float(portfolio_annual_return)


def portfolio_risk(securities, weights):
  df = pd.DataFrame()
  for ticker in securities:
    df[ticker] = yf.download(ticker, period='10y')['Adj Close']
  daily_returns = (df / df.shift(1)) - 1
  annual_risks = daily_returns.std() * (250**0.5)
  portfolio_annual_risk = (np.dot(weights.T, np.dot(daily_returns.cov()*250, weights)))**0.5
  return float(portfolio_annual_risk)
  

