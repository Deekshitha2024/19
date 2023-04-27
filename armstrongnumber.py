n=int(input("enter a number"))
s=0
c=0
temp1=n
temp2=n
while n > 0:
    n=n//10
    c=c+1
while temp1!=0:
    rem=temp1%10
    s=s+rem**c
    temp1=temp1//10
if(temp2==s):
    print("armstrong number")
else:
    print("Not armstrong number")