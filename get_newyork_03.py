#new york
# 40.72, -74.07
#(507,182)
#------------------------------
#college station(284,81)

value=(507,182)
locmapdir='./locationmap3'
locationmap=open(locmapdir,'r')
dict=eval(locationmap.readline())
for num,pair in dict.items():
    if pair==value:
        print 'the num for value is %d'%num
        print num,pair
