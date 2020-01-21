N=input("enter a number in the format XXX-XXX-XXXX:")
for i,c in enumerate(N):
    if i in [3,7]:
        if c=='-':
            n=1
        else:
            n=0

if n==1:
    print("valid")
else:
    print("not")
            
