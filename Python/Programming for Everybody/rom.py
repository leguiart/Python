j=0
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
    for letter in line:              
        if letter!=' ':
            i=i+1  
            continue
        else:
            word=line[j:i]
            word=word.strip()
            li.append(word)
            i=i+1
            j=i
    i=0
    j=0

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