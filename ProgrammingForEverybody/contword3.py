i=0
word=""
while word!="exit+-":
    word=raw_input(">>>")
    if word== "exit+-":
        continue
        
    for letter in word:
        print letter, i
        i=i+1
    print "Number of characters in the string:", i
    i=0