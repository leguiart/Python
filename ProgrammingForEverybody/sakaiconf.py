# Use the file name mbox-short.txt as the file name
sum=0
i=1
while True:
        try:
            file_name=raw_input("Enter file name in file.type format:")
            fhand=open(file_name)
            break
        except:
            print "Enter a valid name and make sure the file is in the same folder as this program"
for line in fhand:
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    else:    
        print line
        zpos=line.find(" ")
        epos=line.find("\n")
        dline=line[zpos:epos]
        dline=dline.strip() 
        dline=float(dline)
        print dline
        print "\n \n"
        sum=dline+sum
        i=i+1
sum=sum/i
print "Average spam confidence:", sum