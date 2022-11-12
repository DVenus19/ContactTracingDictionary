print("~~~~~~~~~~Dictionary - Contact Tracing~~~~~~~~~~")
print("~~~~~~~~~~Programmed by: Donasco,Venus M.~~~~~~~~~~")
print("~~~~~~~~~~BSCOE 2-2~~~~~~~~~~")
#Python Program for Contact Tracing using Dictionary to store info
alldict = {}
while True:
    print('\n\n***************Main Menu:***************\n\n'
    '1.) Add an Item to the Program\n' 
    '2.) Search from the Program\n'
    '3.) Exit(y/n)\n')
    option = input("What do you want to do? (Choice from 1-3): ")
#for option 1
    if option == '1':
        Fullname = input("Add a Full Name: ")
        Age = input("Add the Age: ")
        Address = input("Add the Address: ")
        Phone = input("Add the Phone Number: ")
        item = {
            Fullname : {
                'Age': Age,
                'Address' : Address,
                'Phone' : Phone,
            }
        }
        alldict.update(item)
        print("This contact has been saved,Thank You!!!")

#for option 2
    if option == '2':
        Fullname = input("Search the Fullname that you are looking for: ")
        if Fullname in alldict:
            print("Fullname :", Fullname )
            print("Age : %s" % alldict[Fullname]['Age'])
            print("Address :", alldict[Fullname]['Address'])
            print("Phone : %s" % alldict[Fullname]['Phone'])

#for option 3
    if option == '3':
        exit = input("Exist? (y/n): ")
        if exit == 'y':
            print("Thank You for using this program!")
            break
