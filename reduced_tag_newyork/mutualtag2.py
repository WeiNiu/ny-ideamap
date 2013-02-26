from __future__ import division
import re
#filedir='./reduced_dict_to_0.01_2011_2_newyork_testnew'
filedir='./reduced_dict_to_0.01_total_newyork2'
outfiledir='./similarity_cut_0.1_1'
def MutualTag(dir):
    file = open(dir,'r')
   #file.readline()
    locDict=eval(file.readline())[1]
    print len(locDict)
    outfile=open(outfiledir,'w')
    tagSimilarityDict={}
    vectorSimilarityDict={}
    adoptionTimeDict={}
    for loc1 in locDict.keys():
        #print "this is location"+loc1
        vectorSimilarityDict[loc1]={}
        loc1_x=int(re.split(r'\W+',loc1)[1])
        loc1_y=int(re.split(r'\W+',loc1)[2])
       # print loc1_x,loc1_y
        for loc2 in locDict.keys():
            loc2_x=int(re.split(r'\W+',loc2)[1])
            loc2_y=int(re.split(r'\W+',loc2)[1])
            intersect=[]
            length=0
            totaltagmul=0
            lena_sq=0
            lenb_sq=0
#    print len( locDict[1])
            for item in locDict[loc1].keys():
                #uid intersection
                if item == 'uids':
                    #we ll check the set of same users
                   uidsect = set(locDict[loc1]['uids']).intersection(set(locDict[loc2]['uids']))
                   uidsect=list(uidsect)
                   size_uidsect=len(uidsect)
#                   print size_uidsect
                   if size_uidsect<2:
                       size_uidsect=0
#                   if loc1 != loc2 and size_uidsect != 0:
#                       print>> outfile, loc1,loc2,uidsect
                  
                if locDict[loc2].has_key(item) and item !='uids':
                    intersect.append(item)
                    lena_sq+=locDict[loc1][item]['localcount']**2
                    lenb_sq+=locDict[loc2][item]['localcount']**2
#                    print locDict[loc1]
                    tagmul=locDict[loc1][item]['localcount']*locDict[loc2][item]['localcount']
                    totaltagmul+=tagmul
#            for item in locDict[loc2].keys():
#                if item != 'uids':
#                    lenb_sq+=locDict[loc2][item]['localcount']**2
#            print intersect
            vectorlenmul=(lena_sq**0.5)*(lenb_sq**0.5)
            if totaltagmul==0:
                totaltagmul=0.001
            if vectorlenmul==0:
                vectorlenmul=1      
            #consider Geographical distance in the similarity, the more closer,the more prone to be clustered together.
            roughDist=((85/111*(loc1_x-loc2_x))**2+(loc1_y-loc2_y)**2)**0.5
 #           if roughDist==0:
 #               roughDist=0.1         
            if roughDist>20:
                roughDist=100*roughDist        
            if len(intersect)==0:
                length=1
            else:
                length=len(intersect)
# --------------the following seems unnecessary,didnt show good result---------
           # alldict=[locDict[loc1],locDict[loc2]]
           # union=reduce(lambda x,y:x.union(y.keys()),alldict, set())
#           print union
           # tagsimilarity=len(intersect)/(len(union)-1)
           # if tagsimilarity>=0.3:
           #     print tagsimilarity,loc1,loc2
           # mu=loc1+'-'+loc2
           # tagSimilarityDict[mu]=tagsimilarity
#            print lena_sq,lenb_sq
#            print totaltagmul,vectorlenmul
           # print len(intersect)

          # # vectorSimilarityDict[loc1][loc2]=1/(1/(roughDist**2)*(size_uidsect+1)**3*length**2)
           # print 1000/(roughDist**2)*(size_uidsect+1)**3 
           # print vectorSimilarityDict[loc1][loc2]
            xxx= totaltagmul/vectorlenmul/(len(locDict[loc1])+len(locDict[loc2]))
           # print xxx
            vectorSimilarityDict[loc1][loc2]=1/(1/(roughDist**2)*(size_uidsect+1)**5*(xxx*1000000)**2)
           # vectorSimilarityDict[loc1][loc2]=
#*totaltagmul/vectorlenmul  
#        print>> outfile, tagSimilarityDict
    print>> outfile, vectorSimilarityDict
#        del locDict[loc1]
MutualTag(filedir)
