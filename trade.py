import alpaca_trade_api as tradeapi
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import long_term
from datetime import datetime
from datetime import time
from datetime import timezone

class trading_algorithm():

    #Create a function to signal when to buy and sell
    
    def data(self):
        plt.style.use('fivethirtyeight')

        #Load past Amazon stock data
        self.AMZN = pd.read_csv('AMZNtrain.csv')

        #Plot the adjusted closing price
        plt.figure(figsize = (15, 5))
        plt.plot(self.AMZN['Adj Close'], label = 'AMZN')
        plt.title('Amazon Adj. Close Price History')
        plt.xlabel('Jan. 02, 2014 - Dec. 31, 2018')
        plt.ylabel('Adj. Close Price USD ($)')
        plt.legend(loc = 'upper left')

        #Create a 30 days moving average
        self.average = pd.DataFrame()
        self.average['Adj Close'] = self.AMZN['Adj Close'].rolling(window = 30).mean()

        self.average100 = pd.DataFrame()
        self.average100['Adj Close'] = self.AMZN['Adj Close'].rolling(window = 100).mean()


        plt.figure(figsize = (15, 5))
        plt.plot(self.AMZN['Adj Close'], label = 'AMZN')
        plt.plot(self.average['Adj Close'], label = 'Average 30 days')
        plt.plot(self.average100['Adj Close'], label = 'Average 100 days')
        plt.title('AMZN Adj. Close Price History')
        plt.xlabel('Jan. 02, 2014 - Dec. 31, 2018')
        plt.ylabel('Adj. Close Price USD ($)')
        plt.legend(loc = 'upper left')

        #Create new DataFrame to store all the data
        self.dataset = pd.DataFrame()
        self.dataset['AMZN'] = self.AMZN['Adj Close']
        self.dataset['Average30'] = self.average['Adj Close']
        self.dataset['Average100'] = self.average100['Adj Close']

        def buy_and_sell(data):
            signalToBuy = []
            signalToSell = []
            flag = -1
            for i in range(len(data)):
                if(data['Average30'][i] > data['Average100'][i]):
                    if(flag != 1):
                        signalToBuy.append(data['AMZN'][i])
                        signalToSell.append(np.nan)
                        flag = 1
                    else:
                        signalToBuy.append(np.nan)
                        signalToSell.append(np.nan)
                elif (data['Average30'][i] < data['Average100'][i]):
                    if(flag != 0):
                        signalToBuy.append(np.nan)
                        signalToSell.append(data['AMZN'][i])
                        flag = 0
                    else:
                        signalToBuy.append(np.nan)
                        signalToSell.append(np.nan)
                else:
                    signalToBuy.append(np.nan)
                    signalToSell.append(np.nan)
            return (signalToBuy, signalToSell)

        #Store the buy and sell data
        buy_sell = buy_and_sell(self.dataset)
        self.dataset['Buy Signal Price'] = buy_sell[0]
        self.dataset['Sell Signal Price'] = buy_sell[1]

        #Buy and Sell Strategy
        plt.figure(figsize = (15, 5))
        plt.plot(self.dataset['AMZN'], label = 'AMZN', alpha= 0.35)
        plt.plot(self.dataset['Average30'], label = 'Average 30 days', alpha= 0.35)
        plt.plot(self.dataset['Average100'], label = 'Average 100 days', alpha= 0.35)
        plt.scatter(self.dataset.index, self.dataset['Buy Signal Price'], label = 'Buy', marker = '^', color = 'green')
        plt.scatter(self.dataset.index, self.dataset['Sell Signal Price'], label = 'Sell', marker = 'v', color = 'red')
        plt.title('AMZN Adj. Close History Buy & Sell Signals')
        plt.xlabel('Jan. 02, 2014 - Dec. 31, 2018')
        plt.ylabel('Adj. Close Price USD ($)')
        plt.legend(loc = 'upper left')

    def averageOf30(self):
        self.average = pd.DataFrame()
        self.average['Adj Close'] = self.AMZN['Adj Close'].rolling(window = 30).mean()
        return average
        
    def averageOf100(self):    
        self.average100 = pd.DataFrame()
        self.average100['Adj Close'] = self.AMZN['Adj Close'].rolling(window = 100).mean()
        
    def BuyAndSell(self):
        buying_selling = data.buy_and_sell(self.dataset)
        self.dataset['Buy Signal Price'] = buying_selling[0]
        self.dataset['Sell Signal Price'] = buying_selling[1]
        
    def daily(self):
        barset = self.api.get_barset('AMZN', 'day', limit = 1)
        amzn_bars = barset['AMZN']
        amzn_close = []
        for i in range(len(amzn_bars)):
            x = amzn_bars.__getitem__(i)
            x = x.__getattr__('c')
            AMZN['Adj Close'].append(x)
        averageOf30()
        averageOf100()
        BuyAndSell()
    
    def __init__(self):
        self.key = 'PKGTOT33EQ2IM7YOEZM1'
        self.secret = 'WOQJ87i1aDXxzffpabjMy3AN7vDTh5ClZiGGhYo4'
        self.endpoint = 'https://paper-api.alpaca.markets'
        self.api = tradeapi.REST(self.key, self.secret, self.endpoint)
        self.symbol = 'AMZN'
        self.current_order = None
        self.account = self.api.get_account
        self.last_price = 1
        self.AMZN = None
        self.average = None
        self.average100 = None
        self.dataset = None
        try: 
            self.position = int(self.api.get_position(self.symbol).qty)
        except: 
            self.position = 0

    def submit_order(self):
        if(dataset['Buy Signal Price'][:-1] is not NaN):
            self.current_order = self.api.submit_order(self.symbol, 1, 'buy', 'limit', 'day', self.last_price)
        elif(dataset['Sell Signal Price'][:-1] is not Nan):
            self.current_order = self.api.submit_order(self.symbol, 1, 'sell', 'limit', 'day', self.last_price)
            
def pre_market_open(self) -> bool:
    pre_market_start_time = datetime.now().replace(hour=12, minute=00, second=00, tzinfo=timezone.utc).timestamp()
    market_start_time = datetime.now().replace(hour=13, minute = 30, second = 00, tzinfo=timezone.utc).timestamp()
    right_now = datetime.now().replace(tzinfo=timezone.utc).timestamp()
    
    if(market_start_time >= right_now and right_now >= pre_market_start_time):
        return True
    
    return False

def post_market_open(self) -> bool:
    post_market_end_time = datetime.now().replace(hour=22, minute=30, second=00, tzinfo=timezone.utc).timestamp()
    market_end_time = datetime.now().replace(hour = 20, minute=00, second=00, tzinfo=timezone.utc).timestamp()
    right_now = datetime.now().replace(tzinfo=timezone.utc).timestamp()

    if(post_market_end_time >= right_now and right_now >= market_end_time):
        return True
    
    return False

def regular_market_open(self) -> bool:
    market_start_time = datetime.now().replace(hour=13, minute=30, second=00, tzinfo=timezone.utc).timestamp()
    market_end_time = datetime.now().replace(hour=20, minute=00, second=00, tzinfo=timezone.utc).timestamp()
    
    if market_end_time >= right_now and right_now >= market_start_time:
        return True
    
    return False            

def run_code(trade):
    trade.daily()
    trade.submit_order()
    
def weekend_check(self) -> bool: 
    d = datetime(2020, 12, 25)   
    if(d.weekday() > 4):
        return True
    return False
    
if __name__ == '__main__':
    trade = trading_algorithm()
    trade.data()
    chk = False
    print("running")
    while(True):
        if(regular_market_open == post_market_open and post_market_open == pre_market_open and pre_market_open == False and chk == False and weekend_check == False):
            run_code(trade)
            chk = True
        elif(regular_market_open == post_market_open and post_market_open == pre_market_open and pre_market_open == False): 
            continue
            print("running")
        else:
            chk = False
    print("running")
        
    