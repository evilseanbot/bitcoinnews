import json
from pprint import pprint
json_data=open('bitcoinData.json')

data = json.load(json_data)
print data

TwoDayPrice = float(data[3][1])
OneDayPrice = float(data[4][1])
TodayPrice = float(data[5][1])

def priceDiff(newPrice, oldPrice):
    return (newPrice - oldPrice) / oldPrice



def priceChangeCat(priceChange):
    if priceChange < -0.20:
        return 0
    elif priceChange < -0.10:
        return 1
    elif priceChange < 0.10:
        return 2
    elif priceChange < 0.20:
        return 3
    else:
        return 4

changeCat = priceChangeCat(priceDiff(OneDayPrice, TwoDayPrice))        

if changeCat == 4:
    print "Bitcoin is soaring,",
elif changeCat == 3:
    print "Bitcoin is rising,",
elif changeCat == 2:
    print "Bitcoin is stable,",
elif changeCat == 1:
    print "Bitcoin is falling,",
else:
    print "Bitcoin is crashing,",

print priceDiff(OneDayPrice, TwoDayPrice),

print "but",

changeCat = priceChangeCat(priceDiff(TodayPrice, OneDayPrice))        

if changeCat == 4:
    print "is it destined to soar?",
elif changeCat == 3:
    print "is it likely to rise soon?",
elif changeCat == 2:
    print "is it likely to remain stable?",
elif changeCat == 1:
    print "is it likely to fall soon?",
else:
    print "is it heading for a correction?"

print priceDiff(TodayPrice, OneDayPrice)
