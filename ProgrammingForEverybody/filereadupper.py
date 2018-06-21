# Use words.txt as the file name
while True:
        try:
            file_name=raw_input("Enter file name in file.type format:")
            fhand=open(file_name)
            break
        except:
            print "Enter a valid name and make sure the file is in the same folder as this program"
for line in fhand:
	line=line.strip()
	line=line.upper()
	print line