from twitter import TweetFiles
import os
import json
dir="/home/wei/new_geo_hashtag_data/2011_3.txt"
dictpath= "/home/wei/ideamap/2011_3dict"
path="/home/wei/new_geo_hashtag_data/reduced100000_2011_3"
f=open(dictpath,'r')

path1=""
f1=open(path,'w')
tagdict=f.readline()
tagdict=eval(tagdict)
tagdict1={}
for tag in tagdict.keys():
#    print tag,tagdict[tag]
    if tagdict[tag]>=100000:
        tagdict1[tag]=tagdict[tag]
        print tag,tagdict[tag]


for tweet in TweetFiles.iterateTweetsFromFile(dir):
    for tag in tweet['h']:
        if tag in tagdict1.keys():
            json.dump(tweet,f1)
            f1.write('\n')
            break
