ch=0
i=1
stuff=list()
print 'Enter ch to toggle character off or on'
while True:
    r=raw_input('Enter list elements: ')
    if r=='exit+-':
        break
    if r=='ch':
        if i%2!=0:
            ch=1
            i=i+1
            continue
        else:
            ch=0
            i=i+1
            continue
    if ch==1:
        dpos=r.find('.')
        if dpos!=-1:
            try:
                r=float(r)
                stuff.append(r)
            except:
                stuff.append(r)
                continue
        else:
            try:
                r=int(r)
                stuff.append(r)
            except:
                stuff.append(r)
                continue
    else:
        stuff.append(r)

for i in range(len(stuff)):
    print '\n'
    print i
    print stuff[i] 
print stuff    
print 'List length: ', len(stuff)