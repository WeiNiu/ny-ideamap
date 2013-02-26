from __future__ import division
filedir='/home/wei/ideamap/reduced_tag_newyork/reduced_dict_to_0.01_2011_2_newyork_testnew'
outfiledir='./similarity2011_2_count'
out='./testout'
out=open(out,'w')
def MutualTag(dir):
    file = open(dir,'r')
#    file.readline()
    locDict=eval(file.readline())[1]
    print len(locDict)
    outfile=open(outfiledir,'w')
    tagSimilarityDict={}
    for loc1 in locDict.keys():
#        print "this is location"+loc1
        tagSimilarityDict[loc1]={}
        for loc2 in locDict.keys():
            intersect=[]
#    print len( locDict[1])
            for item in locDict[loc1].keys():
                if locDict[loc2].has_key(item) and item != 'uids':
                    intersect.append(item)
            if loc1=='(14, 16)':
      #           print intersect
                # print locDict[loc1]
                 print locDict[loc2]['uids'] 
                 del locDict[loc2]['uids']
                 for item in locDict[loc2].keys():
                     print>> out, locDict[loc2][item]['localcount']                  
            tagsimilarity=len(intersect)
#            if tagsimilarity==0:
#                print loc1,loc2
    #        tagSimilarityDict[loc1][loc2]=tagsimilarity  
   # print>> outfile, tagSimilarityDict
#       del locDict[loc1]i
    

MutualTag(filedir)
