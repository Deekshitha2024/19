print("1.Area of traingle")
print("2.area of square")
print("3.area of rectangle")
choice=int(input("Enter your choice"))
if choice==1:
    base=int(input("Enter base of traingle"))
    height=int(input("Enter height of the traingle"))
    print("Area is",0.5*base*height)
elif choice==2:
    side=int(input("Enter the side of the square"))
    print("Area is",side*side)
elif choice==3:
    length=int(input("Enter length of the rectangle"))
    breadth=int(input("Enter breadth "))
    print("Area is",length*breadth)
else:
    print("Invalid choice")