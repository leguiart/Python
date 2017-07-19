filehand=open("Sakai.txt")
domain="@uct.ac.za"
for line in filehand:
    line=line.rstrip()
    if not domain in line:
        continue 
    elif domain in line:
        print line
        
        