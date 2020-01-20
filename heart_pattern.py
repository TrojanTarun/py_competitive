n=int(input("enter no of rows:"))
m=int(input("enter no of col:"))

if (n%2==0 and m%2==1):     
    for i in range(6):
        for j in range(7):
            if (i==0 and j%3!=0) or(i==1 and j%3==0) or (i-j==2) or (i+j==8):
                print("*",end=" ")
            else:
                print(end="  ") 
        print()
