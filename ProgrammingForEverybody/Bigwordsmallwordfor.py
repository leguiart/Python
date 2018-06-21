i=0
word=raw_input("Enter word:")
while word!="exit+-":
    for letter in word:
        if i==0:
            big=letter
            small=letter
        else:    
            if letter<big:
                small=letter
            elif letter>big:
                big=letter
        i=i+1
        
    print "Character count:", i
    print "Biggest letter", big
    print "Smallest letter", small
    word=raw_input("Enter word:")
    
        
        
        
        