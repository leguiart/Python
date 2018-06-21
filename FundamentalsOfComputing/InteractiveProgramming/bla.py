n=100
numbers=range(2,n)
results=list()
i=0
while i<n:
    results.append(numbers[i])
    if numbers[i]%results[i]==0:
        numbers.pop(i)
    i=i+1

print len(results)