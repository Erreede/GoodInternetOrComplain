from dbCon import dbCon
from networkMeasure import speedtestData
from complain import twitter
from config.config import twitterComplain

def run():
    resultsdbCon = dbCon.createConnection()
    #Perform speedtest using the Ookla SpeedTest lib
    testResults = speedtestData.performTest()
    if 'png_url' in testResults and twitterComplain:
        #Send the speedtest data to the twitter wrapper to post the message
        twitter.complainOnTwitter(testResults)
    #Save the data in the database
    dbCon.insertResults(resultsdbCon, testResults)
    resultsdbCon.close()

if __name__ == '__main__':
    run()