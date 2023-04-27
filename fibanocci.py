n=int(input(" enter how many series  user wants"))
i=1
if n<0:
    print("Enter positive number")
elif n==0:
    print("0")
else:
    a=0
    b=1
    print(a,b,end=" ")
    while i<=n-2:
        c=a+b
        print(c,end=" ")
        a=b
        b=c
        i=i+1

