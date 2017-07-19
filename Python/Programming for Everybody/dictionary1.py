names=['John', 'Ann', 'Brenton','Royal','Pei','Dena','Patrina','Alane','Dena','Patrina','Hui','Kendrick','Robin','John','John','John','John','Dovie','Elyse','Elyse','Kendrick','Elyse','Hoa','Royal','John','Dena','Royal','Royal','Patrina','Cami','John','Efrain','Cami','John','Yon','Nicholas','Waylon','Reinaldo','Efrain','Efrain','Efrain','Janice']
dct=dict()
least_common=[]
most_name=[]
lst=list()
for name in names:
    if name not in dct:
        dct[name]=1
    else:
        dct[name]=dct[name]+1
        
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
print 'Most common names are: ', most_name 
print 'Repeating:', lst[i-1]
print '\n'
print 'Least common names are: ', least_common
        