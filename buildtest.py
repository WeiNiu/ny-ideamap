from twitter import TweetFiles
#import re
import os
#import json
#dir1='/home/wei/geo_hashtag_data/2011_2.txtr'
#file1='/home/wei/reduced_geo_data/2011_2r'
dir1='/home/wei/new_geo_hashtag_data/reduced1000_2011_3'

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
                loc=CheckLocation(tweet['geo'], 1,-124.77,-66.95,22.52,49.38)
            elif 'bb' in tweet.keys():
                loc=CheckLocation(tweet['bb'], 1,-124.77,-66.95,22.52,49.38)
            #else: pass
            for tag in tweet['h']:
                if tag in CollectionOfHashtags.keys():
                    CollectionOfHashtags[tag]['totalCount']+=1
                else:
                    CollectionOfHashtags[tag]={}
                    CollectionOfHashtags[tag]['totalCount']=1
                    CollectionOfHashtags[tag]['fot']=tweet['t']
                    
                    if  loc not in LocationMap.values():                        #convert location here
                        locationNum+=1
                        LocationMap[locationNum]=loc
                        LocationDict[locationNum]={}
                    lockey=GetKeyFromValue(LocationMap,loc)    
                    CollectionOfHashtags[tag]['fol']=lockey  
            
           # if lockey in LocationDict.keys():
            for tag in tweet['h']:
#                print tag
                if tag not in LocationDict[lockey].keys():
                    LocationDict[lockey][tag]={}
                    LocationDict[lockey][tag]['localcount']=1
                    LocationDict[lockey][tag]['fot']=tweet['t']
                else:
                    LocationDict[lockey][tag]['localcount']+=1
    return (CollectionOfHashtags,LocationDict,LocationMap)                          
f=open('/home/wei/ideamap/reduced_dict_to_1_2011_3','w') 
print >>f, 'this is a test'
print >>f,BuildDataStructure(dir1)       
print >>f,'test over >_<'
f.close()
            
