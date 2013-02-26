from twitter import TweetFiles
#import re
import os
#import json
#dir1='/home/wei/geo_hashtag_data/2011_2.txtr'
#file1='/home/wei/reduced_geo_data/2011_2r'
dir1='/home/wei/ideamap/reduced_tag_newyork/reduced5_2011_2_newyork'

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
                loc=CheckLocation(tweet['geo'], 0.01,-74.38,-73.68,40.46,40.96)
            elif 'bb' in tweet.keys():
  #              print tweet['bb']
                loc=CheckLocation(tweet['bb'], 0.01,-74.38,-73.68,40.46,40.96)
            #else: pass
#            print loc
#            print LocationMap
#            lockey=GetKeyFromValue(LocationMap,loc)
            uid=tweet['user']['id']
            if  loc not in LocationMap.values():                        #convert location here
#                        print locationNum
                locationNum+=1
                LocationMap[locationNum]=loc
                LocationDict[locationNum]={}
                LocationDict[locationNum]['uids']=[]
            lockey=GetKeyFromValue(LocationMap,loc)
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
##############################BUG________________________________________________fixed                    
                  
                       
                    CollectionOfHashtags[tag]['fol']=lockey  
            if uid not in LocationDict[lockey]['uids']:
                LocationDict[lockey]['uids'].append(uid)
                
           # if lockey in LocationDict.keys():
            for tag in tweet['h']:
#                print tag
                if tag not in LocationDict[lockey].keys():
                    LocationDict[lockey][tag]={}
                    LocationDict[lockey][tag]['localcount']=1
                    LocationDict[lockey][tag]['fot']=tweet['t']
                else:
                    LocationDict[lockey][tag]['localcount']+=1

#    print len(LocationDict)
#    for i in LocationDict.keys():
#        print i
    return (CollectionOfHashtags,LocationDict,LocationMap)
#    print len(CollectionOfHashtags.keys())                          
f=open('/home/wei/ideamap/reduced_tag_newyork/reduced_dict_to_0.01_2011_2_newyork_t','w') 
print >>f,BuildDataStructure(dir1)       
f.close()
            
