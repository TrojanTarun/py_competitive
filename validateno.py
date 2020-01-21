import re


n=input("enter  a no:")

if re.match("\d{3}-\d{3}-\d{4}",n):
    print("valid")
else:
    print("not")
