a=int(input("Enter a number"))
b=int(input("Enter b number"))
c=int(input("Enter c number"))
small=0
middle=0
big=0
if a>b and a>c:
    if b > c:
        big=a
        middle=b
        small=c
    else:
        big=a
        middle=c
        small=b
elif b>a and b>c:
    if a>c:
        big=b
        middle=a
        low=c
    else:
        big=b
        middle=c
        low=a
else:
    if a>b:
        big=c
        middle=a
        low=b
    else:
        big=c
        middle=b
        low=a
print(low,middle,big)