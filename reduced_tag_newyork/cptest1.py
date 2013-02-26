from twitter import TweetFiles
import json

dir1 = '/home/wei/ideamap/reduced_tag_newyork/reduced5_2011_2_newyork'
    
def PreprocessingFile(files):
    newfilename=files+'t'
    newfile=open(newfilename,'w')
    n=0
    f=open(files,'r')
    while n<50:
        tweet=f.readline()
        try:
            
            s = newfile.write(tweet)
           # newfile.write("\n")
            n+=1
        except:pass     
    newfile.close()
PreprocessingFile(dir1)
