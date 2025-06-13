tedad_nomerat = int(input("tedad nomerat ro vared kon :"))
nomerat = []
for i in range(0,tedad_nomerat) :
    nomre = int(input("nore ro vared kon :"))
    nomerat.append(nomre)

def mean (list_nomerat , tedad_nomerat) :
    s = sum(list_nomerat) / tedad_nomerat
    return s 
def maxx (list_nomerat) :
    return (max(list_nomerat))

def minn (list_nomerat) :
    return (min(list_nomerat))

print(mean(list_nomerat=nomerat , tedad_nomerat=tedad_nomerat))
m = maxx(nomerat)
print(m)
print(minn(nomerat))