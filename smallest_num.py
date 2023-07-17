def smallnum(l1):
    l2=[]
    for i in range(len(l1)):
        c=0
        for j in range(i+1,len(l1)):
            if l1[i]>l1[j]:
                c+=1
        l2.append(c)  

    return l2      
l1=list(map(int,input().split()))
print(smallnum(l1))