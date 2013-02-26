from __future__ import division
import re

infile='./out10-exp4'
outfile='./clusters10-exp4'

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
            xcor=int(re.split(r'\W+',keys)[1])
#    print something[0]
            ycor=int(re.split(r'\W+',keys)[2])
#    print something[1]
    #print locationnum
   # something=locmap[locationnum] 
            xcor=xcor/100-74.25
# /10 when 0.1 scale
            ycor=ycor/100+40.48
#    print xcor,ycor
            tempdata=[]
            tempdata.append(xcor)
            tempdata.append(ycor)
#                tempdata.append(dict1[keys])
#    if dict1[keys]>0.5:
#        print tempdata
            print tempdata 
            newdict[key].append(tempdata)
    print>>outfile,newdict
