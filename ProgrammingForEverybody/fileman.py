i=0
wordcount=0
lettercount=0
fhand=open("Apuntes Python.txt")
for linea in fhand:
    print linea
    i=i+1
    for word in linea:
        lettercount=lettercount+1
        if word==" ":
            wordcount=wordcount+1
print "Lines:", i
print "Words:", wordcount
print "Letters:", lettercount


    
        
        
        
        