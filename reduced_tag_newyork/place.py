# 500 is new york
file1='./similarity2011_3_count'
file2='./loc65_2011_3_count'
file1=open(file1,'r')
for i in range(1,66):
    s=file1.readline()

file2=open(file2,'w')
print>>file2,s
