#use a rectangle block
from twitter import TweetFiles
#import re
import os
#import json
#dir1='/home/wei/geo_hashtag_data/2011_2.txtr'
#file1='/home/wei/reduced_geo_data/2011_2r'
dir1='/home/wei/ideamap/reduced_tag_newyork/reduced10_total_newyork1'

def LocationQuantize(lowerx,uperx,lowery,upery,scale):
    x=lowerx
    listx=[]
    while x<= uperx:
        listx.append(x);
        x+=scale
    listx.append(x)
    y=lowery
    listy=[]
    while y<=upery:
        listy.append(y);
    listy.append(y)
    
    
def CheckLocation(geo,scale,lowerx,uperx,lowery,upery):
    locationx=0
    locationy=0
    if geo[1]<uperx and geo[1]>lowerx and geo[0]<upery and geo[0]>lowery:
        while geo[1]>lowerx:
            geo[1]-=scale
            locationx+=1
        while geo[0]>lowery:
            geo[0]-=scale
            locationy+=1
    return (locationx,locationy)
    
def GetKeyFromValue(dict,v):
    for key,value in dict.items():
        if value==v:
            return key
    return None
    
def BuildDataStructure(directory):
    CollectionOfHashtags={}
    LocationDict={}
    LocationMap={}
    locationNum=0# the number of loactions
#    listing = os.listdir(directory)
#    for file in listing:
#        print "current file reading is: " + file
#        path=directory+file
    n=0
    for tweet in TweetFiles.iterateTweetsFromFile(directory):
#        print tweet
        n=n+1
        if n%1000==0:
            print n
        if tweet['h']:
#                print tweet['h']
            if 'geo' in tweet.keys():
 #               print tweet['geo']
                loc=CheckLocation(tweet['geo'], 0.01,-74.25,-73.69,40.48,40.96)
            elif 'bb' in tweet.keys():
  #              print tweet['bb']
                loc=CheckLocation(tweet['bb'], 0.01,-74.25,-73.69,40.48,40.96)
            #else: pass
#            print loc
            loc=str(loc)
            uid=tweet['user']['id']
            if loc not in LocationDict.keys():                       
                LocationDict[loc]={}
                LocationDict[loc]['uids']=[]
            if uid not in LocationDict[loc]['uids']:
                LocationDict[loc]['uids'].append(uid)
 #          lockey=GetKeyFromValue(LocationMap,loc)          
            for tag in tweet['h']:
                if tag in CollectionOfHashtags.keys():
                    CollectionOfHashtags[tag]['totalCount']+=1
                    if uid not in CollectionOfHashtags[tag]['uids']:
                        CollectionOfHashtags[tag]['uids'].append(uid)
                else:
                    CollectionOfHashtags[tag]={}
                    CollectionOfHashtags[tag]['uids']=[]
                    CollectionOfHashtags[tag]['totalCount']=1
                    CollectionOfHashtags[tag]['fot']=tweet['t']
                    CollectionOfHashtags[tag]['uids'].append(uid)              
#                   if loc not in LocationDict.keys():                    
#                        LocationDict[loc]={}
#                        LocationDict[loc]['uids']=[]    
                    CollectionOfHashtags[tag]['fol']=loc
#                print tag
#                print LocationDict[loc].keys()
                if tag not in LocationDict[loc].keys():
                    LocationDict[loc][tag]={}
                    LocationDict[loc][tag]['localcount']=1
                    LocationDict[loc][tag]['fot']=tweet['t']
                else:
                    LocationDict[loc][tag]['localcount']+=1 
           # if lockey in LocationDict.keys():
    return (CollectionOfHashtags,LocationDict)                          
#    print len(LocationDict)
#    for i in LocationDict.keys():
#        print i
#    return LocationDict
#    print len(CollectionOfHashtags.keys())
f=open('/home/wei/ideamap/reduced_tag_newyork/reduced_dict_to_0.01_total_newyork1new','w') 
print >>f,BuildDataStructure(dir1)       
f.close()
           
