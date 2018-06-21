i=0
lettercount=0
fhand=open("Apuntes Python.txt")
for linea in fhand:
    print linea
    i=i+1
    lettercount=len(linea)+lettercount
        
print "Lines:", i
print "Letters:", lettercount


    
        
        
        
        