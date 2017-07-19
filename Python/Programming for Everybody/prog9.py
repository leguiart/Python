sum=0
i=0
num=0
while True:
    if num!="ex":
    
        num= raw_input("Enter number, exit with ex:")
        try:
            num= float(num)
            sum= num+sum
            i=i+1
        except:        
            continue
            
        
        
    elif num== "ex":
        num= sum/i
        break
    
print "Average:",num
    
    