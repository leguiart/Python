while True:
    
    names=list()
    dct=dict()
    least_common=[]
    most_name=[]
    lst=list()
    inp=raw_input('Read file / enter line of text / exit (r/t/e)')
    if inp is 'r':
        inp=raw_input('Enter file in .txt form: ')
        try:
            fhand= open(inp)
        except:
            print 'please enter a valid filename'
            continue
    
        for line in fhand:
            line=line.strip()
            names=line.split()
            for name in names:
                dct[name]=dct.get(name,0)+1
            names=[]
        
        for name in dct:
            i=dct[name]
            lst.append(i)
    
        lst.sort()
        i=len(lst)


        for name in dct:
            if dct[name]==lst[0]:
                least_common.append(name)
            elif dct[name]== lst[i-1]:
                most_name.append(name)

        print dct        
        print 'Most common words are: ', most_name 
        print 'Repeating:', lst[i-1]
        print '\n'
        print 'Least common words are: ', least_common
    
    elif inp is 't':
        inp=raw_input('Enter line of text: ')
        inp=inp.strip()
        names=inp.split()
        for name in names:
            dct[name]=dct.get(name,0)+1
           
        for name in dct:
            i=dct[name]
            lst.append(i)
    
        lst.sort()
        i=len(lst)

        for name in dct:
            if dct[name]==lst[0]:
                least_common.append(name)
            elif dct[name]== lst[i-1]:
                most_name.append(name)

        print dct        
        print 'Most common words are: ', most_name 
        print 'Repeating:', lst[i-1]
        print '\n'
        print 'Least common words are: ', least_common
    elif inp is 'e':
        print 'buh bye'
        break            
    else:
        print 'Please enter valid option'
        continue 