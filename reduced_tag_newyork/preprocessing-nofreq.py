from __future__ import division
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
    if temploc[0]>40.48 and temploc[0]<40.96 and temploc[1]>-74.25 and temploc[1]<-73.69:
        if temploc[0]<40.65 or ((30/19)*temploc[1]+157.63)>temploc[0]:               
   # if temploc[0]>40.46 and temploc[0]<40.96 and temploc[1]<-73.68:
            return 1
        else: return 0
    else:return 0
def BoundingH(temploc):    
    if temploc[0]>29.53 and temploc[0]<29.95 and temploc[1]<-95.12 and temploc[1]>-95.67:
        return 1
    else: return 0
class preprocessingTemp:
    def __init__(self):
        self.filecount=0
        self.curfilename=''
   
    @staticmethod
    def PreprocessingFile(files):
	filename=(files.split('reduced_tag_newyork/'))[1]
#	print filename
        newfilename= '/home/wei/ideamap/reduced_tag_newyork/'+filename+'2block'
        newfile=open(newfilename,'w')
        for tweet in TweetFiles.iterateTweetsFromFile(files):	    
#            if tweet['h']:
#            print tweet['h']
            temploc=[]
            if 'geo' in tweet.keys():
                temploc=tweet['geo']
#                    loc=CheckLocation(tweet['geo'], 1, 30,50, -125, -75)
            elif 'bb' in tweet.keys():
                temploc=tweet['bb']
#            print temploc
            if BoundingNewYork(temploc)==1:
#                    loc=CheckLocation(tweet['bb'], 1, 30,50, -125, -75)
                s=json.dump(tweet, newfile)
#                print tweet
                newfile.write("\n")
    @staticmethod            
    def PreprocessingDirectory(directory):
        listing = os.listdir(directory)
        tagdict={}
        for path in listing:
            print "current file is: " + path
            path = directory + path
            print path
            preprocessingTemp.PreprocessingFile(path)
#        tagdictfile=open('./tagdictfile.txt','w')
#        print>>tagdictfile,tagdict
#        return tagdict
dir1='/home/wei/ideamap/reduced_tag_newyork/'            
#preprocessingTemp.PreprocessingDirectory(dir1)
#tagdict={}
preprocessingTemp.PreprocessingFile(dir1+'total.txt')
