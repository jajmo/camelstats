# Bradford Smith (bsmith8)
# CS 521 Project stockReader.py
# 12/01/2016

import csv

class StockThing:

    """
    startDay - m/d/yyyy
    endDay - m/d/yyyy
    return - the difference in the adjusted close price of the stock from startDay
             to endDay as a flot, or the strings 'Invalid startDay' or 'Invalid
             endDay' if either the start or end day could not be found
    """
    def getStockChange(startDay, endDay):
        startPrice = None
        endPrice = None

        with open('tsla_stock.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for line in reader:
                #print(line['Date'], line['Open'], line['Adj Close'])
                if line['Date'] == startDay:
                    startPrice = line['Adj Close']
                if line['Date'] == endDay:
                    endPrice = line['Adj Close']
        csvfile.close()

        if (startPrice == None):
            return 'Invalid startDay'
        elif(endPrice == None):
            return 'Invalid endDay'
        else:
            return float(endPrice) - float(startPrice)
