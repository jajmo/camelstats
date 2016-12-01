# Bradford Smith (bsmith8)
# CS 521 Project stockReader.py
# 12/01/2016

import csv

class StockThing:

    """
    startDay - m/d/yyyy
    endDay - m/d/yyyy
    return - the difference in the adjusted close price of the stock from
             startDay to endDay as a float, or the strings 'Invalid startDay' or
             'Invalid endDay' if either the start or end day could not be found
    """
    def getStockChange(startDay, endDay):
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

        with open('tsla_stock.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for line in reader:
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
