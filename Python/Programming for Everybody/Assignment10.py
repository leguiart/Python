dct=dict()
lst=list()

name = raw_input("Enter file:")
if len(name) < 1 : 
    name = "mbox-short.txt"
handle = open(name)
for line in handle:
    if line is ' ':
        continue
    if line.startswith('From '):
        line=line.strip()
        lst=line.split()
        if len(lst)==7:
            word=lst[5]
            word=word.split(':')
            word= word[0]
            dct[word]=dct.get(word,0)+1
    lst=[]
lst=list()
for i, j in dct.items():
    lst.append((i,j)) 

lst.sort()

for i, j in lst:
    print i,j
        
