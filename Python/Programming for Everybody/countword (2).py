w=""
while w=!"exit+-":
    w=raw_input("Enter word:")
    i=0
    while True:
        try:
            w[i]
            i=i+1
        except:
            break
    print i

        