from dbCon import dbCon
from networkMeasure import speedtestData
from complain import twitter
from config.config import twitterComplain

def run():
    resultsdbCon = dbCon.createConnection()
    #Perform speedtest using the Ookla SpeedTest lib
    testResults = speedtestData.performTest()
        
    #Save the data in the database
    if len(testResults) > 0: 
        if twitterComplain:
            twitter.complainOnTwitter(testResults)
        dbCon.insertResults(resultsdbCon, testResults)
    resultsdbCon.close()

if __name__ == '__main__':
    run()