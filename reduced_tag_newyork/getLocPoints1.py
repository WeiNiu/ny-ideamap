from __future__ import division
import re
# from the locationMap nad mutual hashtag relationship 
locationfiledir='./similarity2011_2_count'
#locationmapdir='./locationmap3'
datafiledir='./finaldata_count'
#locmap=open(locationmapdir,'r')
locfile=open(locationfiledir,'r')
datafile=open(datafiledir,'w')
#dict1=locfile.readline()
dict=eval(locfile.readline())
print dict.keys()
dict1=dict['(54, 24)']
#print dict1
#locmap=eval(locmap.readline())
data=[]
#something=[]
for keys in dict1.keys():
    print keys
    xcor=int(re.split(r'\W+',keys)[1])
#    print something[0]
    ycor=int(re.split(r'\W+',keys)[2])
#    print something[1]
    #print locationnum
   # something=locmap[locationnum] 
    xcor=xcor/100-74.38
# /10 when 0.1 scale
    ycor=ycor/100+40.46
#    print xcor,ycor
    tempdata=[]
    tempdata.append(xcor)
    tempdata.append(ycor)
    tempdata.append(dict1[keys])
    if dict1[keys]>0.5:
        print tempdata
        
    data.append(tempdata)
print>> datafile,data   
