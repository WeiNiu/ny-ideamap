
import cjson,gzip
from datetime import datetime

twitter_api_time_format = '%a %b %d %H:%M:%S +0000 %Y'

class TweetFiles:
    @staticmethod
    #generator
    def iterateTweetsFromFile(file):
        for line in open(file,'rb'):
            try:
                data = cjson.decode(line)
#                data = cjson.decode(data)
##                read one line each time and return. notice the difference between yield and return.
##                to avoid read all tweets into the memory at one time
                if 'tx' in data: yield data
            except: pass
            
#file1='/home/wei/Downloads/tweets/hashtag/2011_2r'
#for tweet in TweetFiles.iterateTweetsFromFile(file1):
#    print tweet['tx']
#for data in FileIO.iterateJsonFromFile(file):
    
        
def getDateTimeObjectFromTweetTimestamp(timeStamp): return datetime.strptime(timeStamp, twitter_api_time_format)
def getStringRepresentationForTweetTimestamp(timeStamp): return datetime.strftime(timeStamp, twitter_api_time_format)
