#for relationship between no. of hashtags and no. of locations
dictfile=open('reduced_dict2011_11','r')
dictfile.readline()
dict=eval(dictfile.readline())
#print dict[1]
freq={}
for place in dict[1].keys():
#    print place
#    print dict[1][place]
    if len(dict[1][place]) not in freq.keys():
        freq[len(dict[1][place])]=1
    else: freq[len(dict[1][place])]+=1
freqdict=open('2011_11_loc_tag_freq','w')
print>> freqdict, freq
