n = int(input("addad : "))
l = []
for i in range(1,n+1) :
    for j in range(1,n+1) :
        s = i*j
        l.append(s)
    print(l)
    l.clear()