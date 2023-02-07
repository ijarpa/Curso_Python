from project_finance import read_csv
import pytest

import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import csv
import random


stocksroe = []
def read_csv(filename):
    stocklist = []
    companies = []
    with open (filename, 'rt') as stocks_sp500: #read the companies of s&p 500
        reader = csv.reader(stocks_sp500)
        for i in stocks_sp500:
            line = i.split(';')
            stocklist.append(line[1])

        for i in range(len(stocklist)):
            number = random.randint(0, len(stocklist)-1)

            if stocklist[number] not in companies:
                companies.append(stocklist[number])

    companies = companies[0:4]
    return companies

read_csv('./list_stocks.csv')
