count=0
while True:
    try:
        rfile=raw_input('Enter file name in file.txt format: ')
        fh=open(rfile)
        break
    except:
        print 'Enter a valid file name'
        continue

for line in fh:
    line=line.strip()
    if line=='':
        continue
    if line.startswith('From '):
        count=count+1
        words=line.split()
        print words[1]

print "There were", count, "lines in the file with From as the first word"
