filedir='./reduced_dict_to_1_2011_3'
outfiledir='./locationmap3_to1'

def GetLocationMap(dir):
    openfile=open(dir,'r')
    openfile.readline()
    locMap=eval(openfile.readline())[2]
    print len(locMap)
    outfile=open(outfiledir,'w')
    print >>outfile, locMap
    return locMap

GetLocationMap(filedir)
