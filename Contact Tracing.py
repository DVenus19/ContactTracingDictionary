print("~~~~~~~~~~Dictionary - Contact Tracing~~~~~~~~~~")
print("~~~~~~~~~~Programmed by: Donasco,Venus M.~~~~~~~~~~")
print("~~~~~~~~~~BSCOE 2-2~~~~~~~~~~")
#Python Program for Contact Tracing using Dictionary to store info
alldict = {}
while True:
    print('Menu: 1. Add an item , 2. Search , 3. Exit(y/n)')
    option = input("What do you want to do? (1-3)")
#for option 1
    if option == '1':
        fullname = input("Add the Fullname: ")
        age = input("Add the Age: ")
        address = input("Add the Address: ")
        phone = input("Add the Phone Number: ")

