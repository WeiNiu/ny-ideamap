filedir='./reduced_dict_to_0.01_2011_3_newyork'
outfiledir='./locationmap3_to'

def GetLocationMap(dir):
    openfile=open(dir,'r')
    openfile.readline()
    locMap=eval(openfile.readline())[2]
    print len(locMap)
    outfile=open(outfiledir,'w')
    print >>outfile, locMap
    return locMap

GetLocationMap(filedir)
