import urllib2, StringIO, csv, datetime
import json

def getBtcList (time = False):

    if (time != False):
        url = 'http://api.bitcoincharts.com/v1/trades.csv?symbol=mtgoxUSD&start=' + str(time)
    else:
        url = 'http://api.bitcoincharts.com/v1/trades.csv?symbol=mtgoxUSD'
    
    response = urllib2.urlopen(url).read()
    output = StringIO.StringIO(response)
    cr = csv.reader(output)

    btcList = cr.next()
    return btcList

def printTradeTimes(btcList):
    print "First trade time: " + (datetime.datetime.fromtimestamp(int(btcList[0])).strftime('%Y-%m-%d %H:%M:%S'))
    

btcLists = []
    
btcList = getBtcList()

btcLists.append(btcList)

for i in range (4):
    nextDay = int(btcList[0]) + 86400
    btcList = getBtcList(nextDay)
    btcLists.append(btcList)

nextDay = int(btcList[0]) + 82800
btcList = getBtcList(nextDay)
btcLists.append(btcList)

print btcLists

with open('bitcoinData.json', 'w') as outfile:
  json.dump(btcLists, outfile)
