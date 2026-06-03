class StockSpanner(object):

    def __init__(self):
        self.stocks = []
    def next(self, price):
        span=1
        while self.stocks and self.stocks[-1][0]<=price:
            span += self.stocks[-1][1]
            self.stocks.pop()
        self.stocks.append([price, span])
        return span
        
        
