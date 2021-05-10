n=int(input())
list1=[]
k=1
for i in range(n):
    if i%2==0:
        for j in range(5):


            print(k,end=" ")
            k=k+1
            
    else:
        for j in range(5):
            list1.append(k)

            k=k+1
        list1.reverse()
        for l in range(5):
            print(list1[l],end=" ")
    list1=[]
    print("")
