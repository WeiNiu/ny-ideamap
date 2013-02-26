from __future__ import division
filedir='./reduced_dict_to_0.01_2011_2_newyork'
outfiledir='./similarity2011_2_to1'
def MutualTag(dir):
    file = open(dir,'r')
    file.readline()
    locDict=eval(file.readline())[1]
    print len(locDict)
    outfile=open(outfiledir,'w')
    for loc1 in locDict.keys():
        print "this is location"+str(loc1)
        tagSimilarityDict={}
        vectorSimilarityDict={}
        adoptionTimeDict={}
        for loc2 in locDict.keys():
            intersect=[]
            totaltagmul=0
            lena_sq=0
            lenb_sq=0
#    print len( locDict[1])
            for item in locDict[loc1].keys():
                if locDict[loc2].has_key(item):
                    intersect.append(item)
#                    tagmul=locDict[loc1][item]['localcount']*locDict[loc2][item]['locolcount']
 #                   totaltagmul+=tagmul
  #                  lena_sq+=locDict[loc1][item]['localcount']**2
  #                  lenb_sq+=locDict[loc2][item]['localcount']**2
#            print intersect
   #         vectorlenmul=(lena_sq**0.5)*(lenb_sq**0.5) 
                        
            alldict=[locDict[loc1],locDict[loc2]]
            union=reduce(lambda x,y:x.union(y.keys()),alldict, set())
#           print union
            tagsimilarity=len(intersect)/len(union)
            if tagsimilarity>=0.3:
                print tagsimilarity,loc1,loc2
            mu=str(loc1)+'-'+str(loc2)
            tagSimilarityDict[mu]=tagsimilarity
            vectorSimilarityDict[mu]=totaltagmul/vectorlenmul  
        print>> outfile, tagSimilarityDict
#        del locDict[loc1]

MutualTag(filedir)
