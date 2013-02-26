from twitter import TweetFiles
import os
import json
import re
class preprocessingTemp:
    def __init__(self):
        self.filecount=0
        self.curfilename=''
   
    @staticmethod
    def PreprocessingFile(files,tagdict):
	filename=(files.split('reduced_geo/'))[1]
#	print filename
        newfilename= '/home/wei/new_geo_hashtag_data/'+filename +'.txt'
        newfile=open(newfilename,'w')
        for tweet in TweetFiles.iterateTweetsFromFile(files):
	    
            if tweet['h']:
#		print tweet['h']
                temploc=[]
                if 'geo' in tweet.keys():
                    temploc=tweet['geo']
#                    loc=CheckLocation(tweet['geo'], 1, 30,50, -125, -75)
                elif 'bb' in tweet.keys():
                    temploc=tweet['bb']
                #print temploc
                if temploc[0]>24.52 and temploc[0]<49.38 and temploc[1]<-66.95 and temploc[1]>-124.77:
#                    loc=CheckLocation(tweet['bb'], 1, 30,50, -125, -75)
                    for tag in tweet['h']:
                        if tag not in tagdict.keys():
                            tagdict[tag]=1
                        else:tagdict[tag]+=1
                    s=json.dump(tweet, newfile)
                    newfile.write("\n")
    @staticmethod            
    def PreprocessingDirectory(directory):
        listing = os.listdir(directory)
        tagdict={}
        for path in listing:
            print "current file is: " + path
            path = directory + path
            print path
            preprocessingTemp.PreprocessingFile(path,tagdict)
        tagdictfile=open('./tagdictfile.txt','w')
        print>>tagdictfile,tagdict
        return tagdict
dir1='/mnt/chevron/dataset/twitter/reduced_geo/'            
#preprocessingTemp.PreprocessingDirectory(dir1)
tagdict={}
preprocessingTemp.PreprocessingFile(dir1+'2011_11',tagdict)
