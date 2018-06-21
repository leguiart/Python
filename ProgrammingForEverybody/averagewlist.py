i=0
li=list()
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
        li.append(inp)
    else: 
        inp=int(inp)
        li.append(inp)
average=(sum(li))/(len(li))
print 'Average: ', average