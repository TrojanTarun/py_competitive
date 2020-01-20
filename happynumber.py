def ishapy(num):
    r=s=0
    while(num>0):
        r=num%10
        s=s+(r*r)
        num=num//10
    return s
num=int(input("enter a number:"))
n=num
while(n!=1 and n!=4):
    n = ishapy(n) 
if(n==1):
    print("happy")
else:
    print("not")






