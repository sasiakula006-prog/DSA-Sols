class StockSpanner(object):

    def __init__(self):
        self.stocks = []
    def next(self, price):
        span=1
        while self.stocks and self.stocks[-1][0]<=price:
            _,p = self.stocks.pop()
            span += p
        self.stocks.append([price,span])
        return span
        
        
