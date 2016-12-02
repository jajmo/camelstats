# Bradford Smith (bsmith8)
# CS 521 Project stockReader.py
# 12/01/2016

import csv

class StockThing:

    def __init__(self):
        self.date_closeprice = {}
        with open('data/tsla_stock.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for line in reader:
                self.date_closeprice[line['Date']] = line['Adj Close']

    """
    startDay - m/d/yyyy
    endDay - m/d/yyyy
    return - the difference in the adjusted close price of the stock from
             startDay to endDay as a float, or the strings 'Invalid startDay' or
             'Invalid endDay' if either the start or end day could not be found
    """
    def getStockChange(self, startDay, endDay):
        startPrice = None
        endPrice = None

        startDaySplit = startDay.split('/')
        endDaySplit = endDay.split('/')

        if int(startDaySplit[0]) < 10:
            startDaySplit[0] = startDaySplit[0][1:]
        if int(startDaySplit[1]) < 10:
            startDaySplit[1] = startDaySplit[1][1:]

        if int(endDaySplit[0]) < 10:
            endDaySplit[0] = endDaySplit[0][1:]
        if int(endDaySplit[1]) < 10:
            endDaySplit[1] = endDaySplit[1][1:]

        startDay = '/'.join(startDaySplit)
        endDay = '/'.join(endDaySplit)

        startPrice = self.date_closeprice.get(startDay, None)
        endPrice = self.date_closeprice.get(endDay, None)

        if (startPrice == None):
            return 'Invalid startDay'
        elif(endPrice == None):
            return 'Invalid endDay'
        else:
            return float(endPrice) - float(startPrice)
