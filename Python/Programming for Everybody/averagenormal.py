i=0
sum=0
print 'Enter a single float if you want decimal number'
while True:
    inp=raw_input('Enter values: ')    
    if inp=='exit': break
    try:
        float(inp)
    except:
        print 'please enter only numeric values'
        continue        
    i=i+1
    dpos=inp.find('.')
    if dpos!=-1:
        inp=float(inp)       
    else: 
        inp=int(inp)
    sum=inp+sum
av=sum/i
print 'Average', av