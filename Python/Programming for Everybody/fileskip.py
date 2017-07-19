i=0
wordcount=0
lettercount=0
l=0
s=0
wcounttwo=0
while True:
    while True:
        try:
            file_name=raw_input("Enter file name in file.type format or state if you want to exit by entering exit+-:")
            if file_name=="exit+-":
                break
            fhand=open(file_name)
            break
        except:
            print "Enter a valid name and make sure the file is in the same folder as this program"
    if file_name=="exit+-":
        break    
    for linea in fhand:
        linea=linea.strip()
        if linea.startswith("Ej"): 
            print "Ej",s+1 
            for linea in fhand:
                linea=linea.strip()
                if l==0:
                    s=s+1    
                print linea
                l=l+1
                if l>=10:
                    print "\n \n"
                    break
                elif linea.startswith("Ej"):
                    l=0
                    continue
        i=i+1
        wcounttwo= wcounttwo+l
        l=0
        for word in linea:
            lettercount=lettercount+1
            if word==" ":
                wordcount=wordcount+1
    print "Lines:", i
    print "Words:", wordcount
    print "Letters:", lettercount
    print "Number of examples:", s
    print "Numer of lines of examples", wcounttwo



    
        
        
        
        