from __future__ import division
import re
# from the locationMap nad mutual hashtag relationship 
locationfiledir='./loc500_2011_3'
locationmapdir='./locationmap3'
datafiledir='./finaldata_500'
locmap=open(locationmapdir,'r')
locfile=open(locationfiledir,'r')
datafile=open(datafiledir,'w')
#dict1=locfile.readline()
dict1=eval(locfile.readline())
locmap=eval(locmap.readline())
data=[]
for keys in dict1.keys():
    locationnum =int(re.split(r'-',keys)[1])
    print locationnum
    something=locmap[locationnum] 
    xcor=something[0]/10-124.77
# /10 when 0.1 scale
    ycor=something[1]/10+22.52
#    print xcor,ycor
    tempdata=[]
    tempdata.append(xcor)
    tempdata.append(ycor)
    tempdata.append(dict1[keys])
    if dict1[keys]>0.5:
        print tempdata
        
    data.append(tempdata)
print>> datafile,data   
