class Book:
    numberOfPages=145
    author="DEEksha"
    scope="to be sold in india"
    def __init__(self,zone,dob):
        self.zone=zone
        self.dob=dob
    def __del__(self):
        print("destructor is called")
my_book=Book("mystery","10-10-2023")
print(my_book.author)
print(my_book.zone)
del my_book
