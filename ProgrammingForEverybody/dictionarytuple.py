while True:
    lst=list()
    names=list()
    dct=dict()
    inp=raw_input('Read file / enter line of text / exit (r/t/e)')
    most_name= []
    least_common= []
    if inp is 'r':
        inp=raw_input('Enter file in .txt form: ')
        try:
            fhand= open(inp)
        except:
            print 'please enter a valid filename'
            continue
    
        for line in fhand:
            if line is ' ':
                continue
            line=line.strip()
            names=line.split()
            for name in names:
                dct[name]=dct.get(name,0)+1
            names=[]
            
        for i,j in dct.items():
            lst.append((j,i))
            
        lst.sort(reverse=True)
        if len(lst)>=10:
            print '\n'
            print 'Most common words are:  \n' 
            for i,j in lst[:10]:
                print j, i
            k=(len(lst))-1
            print '\n'
            print 'Least common words are: ', 
            print '\n'
        
            for i,j in lst[k-9:k+1]:
                print j,i
       
        print lst        
    
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