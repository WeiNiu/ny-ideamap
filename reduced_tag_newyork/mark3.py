#from __future__ import division
#import re
from geo import UTMConverter
infile='./out10'
outfile='./clusters10'

infile=open(infile,'r')
outfile=open(outfile,'w')

for i in range(2,20):
    infile.readline()
    dict=eval(infile.readline())
    newdict={}
    for key in dict.keys():
        newdict[key]=[]
        for keys in dict[key]:
            print keys              
            corr=UTMConverter.UTMtoLL(keys)                    
#            tempdata=[]
#            tempdata.append(xcor)
#            tempdata.append(ycor)
#                tempdata.append(dict1[keys])
#    if dict1[keys]>0.5:
#        print tempdata
#            print tempdata 
            newdict[key].append(corr)
    print>>outfile,newdict
