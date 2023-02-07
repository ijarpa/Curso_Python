import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import csv
import random

# list of companies are in the .csv file called: list_stocks.csv

stocksroe = []
def read_csv(filename):
    stocklist = []
    companies = []
    with open (filename, 'rt') as stocks_list: #read the companies of s&p 500
        reader = csv.reader(stocks_list)
        for i in stocks_list:
            line = i.split(';')
            stocklist.append(line[1])

        for i in range(len(stocklist)):
            number = random.randint(0, len(stocklist)-1)

            if stocklist[number] not in companies:
                companies.append(stocklist[number])

    companies = companies[0:4]
    return companies
    #return stocklist

def RoE(ticker):

    try:
        data = yf.Ticker(ticker)
        roe = data.info['returnOnEquity'] #roe
        name = data.info['shortName'] #company name
        symbol = data.info['symbol'] #symbol
        roe_list = [name, symbol, roe]
        if roe_list not in stocksroe:
            stocksroe.append(roe_list)
        print(name, ":", roe)

    except KeyError as key:
        print(f"Value {key} not found, please run the program again")



def return_portfolio(stocks, weights):
    historical_data = yf.download(stocks, start='2018-01-01') #download data from date selected
    close_price = historical_data['Close'].pct_change() #percentage of return between open price and close price
    portfolio_return = (close_price * weights).sum(axis=1)
    cumulative_return = (portfolio_return + 1).cumprod()

    portfolio_weights=[]
    portfolio_returns=[]
    portfolio_risk=[]
    portfolio_sharpe=[]

    def optimization(close):
        random_stocks = np.random.uniform(size=len(close.columns))
        random_stocks = random_stocks / np.sum(random_stocks)

        portfolio_weights.append(random_stocks) #portfolio percentage

        mean = (close.mean() * random_stocks).sum() * 252 #return
        portfolio_returns.append(mean)

        volatility = (close * random_stocks).sum(axis=1) #portfolio risk 
        annual_std = np.std(volatility) * np.sqrt(252)
        portfolio_risk.append(annual_std)

        sharpe_ratio = (np.mean(volatility) / np.std(volatility)) * np.sqrt(252)
        portfolio_sharpe.append(sharpe_ratio)
        
    #data visualization
    x = cumulative_return.keys()
    y = cumulative_return

    fig, ax = plt.subplots(figsize=(21,6))
    ax.plot(x, y, linewidth=2.0)
    ax.set_title('Cumulative Portfolio Return')

    plt.show() 


    count = 1000
    for k in range(0, count):
        optim = optimization(close_price)

    max_sharpe_ratio = np.argmax(portfolio_sharpe) #The Sharpe ratio compares the return of an investment with its risk
    max_portfolio_weights = portfolio_weights[max_sharpe_ratio]
    print(f"Max sharpe ratio: {portfolio_sharpe[max_sharpe_ratio]:.2f}")

    print("\nportfolio")
    for i in range(len(max_portfolio_weights)):
        print(f"{close_price.columns[i]}: {max_portfolio_weights[i]:.3f}")

    #Composition portfolio 
    x = close_price.columns
    y = max_portfolio_weights

    fig, ax = plt.subplots(figsize=(12,6))
    ax.bar(x, y)
    ax.set_title('Portfolio Distribution')

    plt.show()


    #Efficient Frontier
    max_ratio = max_sharpe_ratio

    x = portfolio_risk
    y = portfolio_returns

    fig, ax = plt.subplots(figsize=(12,6))
    ax.scatter(x, y, c=portfolio_sharpe, cmap='winter') #Efficient Frontier between risk and return
    ax.set_title('Efficient Frontier & Sharpe Ratio', fontsize=25)

    plt.xlabel("Risk", fontsize=20)
    plt.ylabel("Return", fontsize=20)
    plt.scatter(x[max_ratio], y[max_ratio], color='r', marker='o', s=300) #sharpe ratio
    plt.colorbar(label='Sharper ratio')

    plt.show ()

def main():
    print("\nReturn of investment for company: ")
    for i in read_csv('list_stocks.csv'):
        RoE(i)

    list_companies = list(map(lambda x: x[1], stocksroe))
    stocks = list_companies
    weights = [0.25, 0.25, 0.25, 0.25] #percentage of the components in portfolio
    return_portfolio(stocks, weights)

if __name__ == "__main__":
    main()