from twitter import TweetFiles
import os
import json
dir="/home/wei/ideamap/reduced_tag_newyork/total.txt1"
dictpath= "/home/wei/ideamap/reduced_tag_newyork/total.txtdict"
path="/home/wei/ideamap/reduced_tag_newyork/reduced10_total_newyork4"
#dictpath1='/home/wei/ideamap/reduced_tag_newyork/2011_2reduceddict'
f=open(dictpath,'r')
f1=open(path,'w')
#f2=open(dictpath1,'w')
tagdict=f.readline()
tagdict=eval(tagdict)
tagdict1={}
taglist=[]
for tag in tagdict.keys():
#    print tag,tagdict[tag]
    if tagdict[tag]>=10:
        tagdict1[tag]=tagdict[tag]
#        print tag,tagdict[tag]
#print >>f2, taglist

for tweet in TweetFiles.iterateTweetsFromFile(dir):
    for tag in tweet['h']:
        if tag in tagdict1.keys():
            json.dump(tweet,f1)
            f1.write('\n')
            break 
