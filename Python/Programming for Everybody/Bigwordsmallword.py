i=0
word=raw_input("Enter word:")
while word!="exit+-":
    while i<len(word):
        if i==0:
            big=word[i]
            small=word[i]
        else:    
            if word[i]<big:
                small=word[i]
            elif word[i]>big:
                big=word[i]
        i=i+1
    print "Letter count:", i
    print "Biggest letter", big
    print "Smallest letter", small
    word=raw_input("Enter word:")
    
        
        
        
        