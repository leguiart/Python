dct=dict()
lst=list()
i=0
j=0

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
        word=lst[4]
        dct[word]=dct.get(word,0)+1
    lst=[]
        
big_address= None
big_number= None

for i,j in dct.items():
    if big_number is None or big_number<j:
        big_address= i
        big_number= j
        
       
        
print big_address,big_number
        
