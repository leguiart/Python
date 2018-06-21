def merge(line):
    lst=[0]*4
    lst1=[0]*4
    lst2=[0]*4
    count=0
    mergeable=False
    for i in range(len(line)):
        if line[i]!=0:
            lst[count]=line[i]
            count+=1
    for i in range(len(lst)):
        if mergeable and lst[i]==lst[i-1]:
            lst1[i-1]=lst[i]*2
            lst1[i]=0
            mergeable=False
        else:
            lst1[i]=lst[i]
            mergeable=True
    count=0       
    for i in range(len(lst1)):
        if lst1[i]!=0:
            lst2[count]=lst1[i]
            count+=1    
    return lst2


print merge([4,2,2,4])
print merge([8,16,16,8])
print merge([4,4,2,2])
print merge([8,8,8,2])