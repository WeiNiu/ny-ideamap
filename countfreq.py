dictfile=open('2011_11dict','r')
dict=eval(dictfile.readline())
freq={}
for item in dict.values():
    if item not in freq.keys():
        freq[item]=1
    else: freq[item]+=1
freqdict=open('2011_11freqdict','w')
print>> freqdict, freq
#return freq

