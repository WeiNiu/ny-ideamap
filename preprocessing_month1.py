from twitter import TweetFiles
import os
import json
import re
def BoundingUS(temploc):    
    #print temploc
    if temploc[0]>24.52 and temploc[0]<49.38 and temploc[1]<-66.95 and temploc[1]>-124.77:
        return 1
    else:return 0
def BoundingNewYork(temploc):
    if temploc[0]>40.46 and temploc[0]<40.96 and temploc[1]>-74.38 and temploc[1]>-73.68:
        return 1
    else:return 0
    


class preprocessingTemp:
    def __init__(self):
        self.filecount=0
        self.curfilename=''
   
    @staticmethod
    def PreprocessingFile(files,tagdict):
    	filename=(files.split('reduced_geo/'))[1]
#	    print filename
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
               # if temploc[0]>24.52 and temploc[0]<49.38 and temploc[1]<-66.95 and temploc[1]>-124.77:
#                  loc=CheckLocation(tweet['bb'], 1, 30,50, -125, -75)
#                if BoundingUS(temploc)==1:
                if BoundingNewYork(temploc)==1:
                    for tag in tweet['h']:
                        if tag not in tagdict.keys():
                            tagdict[tag]=1
                        else:tagdict[tag]+=1
                    s=json.dump(tweet, newfile)
                    newfile.write("\n")
        tagdictfile=open('./'+filename+'dict','w')
        print>>tagdictfile,tagdict
        return tagdict

    @staticmethod            
    def PreprocessingDirectory(directory):
        listing = os.listdir(directory)
        for path in listing:
            tagdict={}
            print "current file is: " + path
            path = directory + path
            print path
            preprocessingTemp.PreprocessingFile(path,tagdict)
dir1='/mnt/chevron/dataset/twitter/reduced_geo/'            
#preprocessingTemp.PreprocessingDirectory(dir1)
#preprocessingTemp.PreporcessingFile(dir1+'2011_10')
tagdict={}
preprocessingTemp.PreprocessingFile(dir1+'2011_2',tagdict)
