n=int(input("enter number of products:"))
a=0
b=0
for i in range(n):
    a[i]=int(input("enter spoilage"))
    b[i]=int(input("enter spoilage"))
    while n>=3 and n<=5:
        u=v=0
        if(a[i]>=1 and b[i]<=30): 
            u=u+a[i]
            v=v+b[i]
        m=u//v
print(m)





