i=0
li=list()
while True:
    try:
        rfile=raw_input('Enter file name in file.txt format: ')
        fh=open(rfile)
        break
    except:
        print 'Enter a valid file name'
        continue
for line in fh:
    line=line.rstrip()
    words=line.split()
    for word in words:    
        li.append(word)

li.sort()
lidos=list()
for word in li:
    if i==0:
        i=i+1
        lidos.append(word)
        continue   
    if word!=li[i-1]:
        lidos.append(word)
    i=i+1

print lidos           