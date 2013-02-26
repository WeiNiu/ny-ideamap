from __future__ import division
filedir='/home/wei/ideamap/reduced_dict_to_1_2011_3'
outfiledir='./similarity2011_3_to1'
def MutualTag(dir):
    file = open(dir,'r')
    file.readline()
    locDict=eval(file.readline())[1]
    print len(locDict)
    outfile=open(outfiledir,'w')
    for loc1 in locDict.keys():
        print "this is location"+str(loc1)
        tagSimilarityDict={}
        for loc2 in locDict.keys():
            intersect=[]
#    print len( locDict[1])
            for item in locDict[loc1].keys():
                if locDict[loc2].has_key(item):
                    intersect.append(item)
#            print intersect             
            alldict=[locDict[loc1],locDict[loc2]]
            union=reduce(lambda x,y:x.union(y.keys()),alldict, set())
#           print union
            tagsimilarity=len(intersect)/len(union)
            if tagsimilarity>=0.5:
                print tagsimilarity,loc1,loc2
            mu=str(loc1)+'-'+str(loc2)
            tagSimilarityDict[mu]=tagsimilarity  
        print>> outfile, tagSimilarityDict
#        del locDict[loc1]

MutualTag(filedir)
