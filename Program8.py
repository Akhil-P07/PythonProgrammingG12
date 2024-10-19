#Program to create binary file to store Rollno and Name, 
# Search any Rollno and display name if Rollno found otherwise “Rollno not found
import pickle
data = dict()

def enterData():
    file = open("Program8.txt", 'wb')
    n  = int(input("Enter no. of entries: "))
    for i in range(n):
        rollNo = int(input("Enter roll no. "))
        name = input("Enter name: ")
        data["Student entry #%i"%(i + 1)] = [rollNo, name]
    pickle.dump(data, file)
    file.close()
def seekData(rollNo):
    file = open("Program8.txt", "rb")
    data = pickle.load(file)
    for key in data:
        value = data.get(key)
        if value[0] == rollNo:
            return value[1]
    
    return "Rollno not found"

option = int(input("Would you like to:\n1. Seek data - Press 0\n2. Enter data - Press 1\nChoose: "))

if option == 0:
    rollno = int(input("Enter roll no: "))
    name = seekData(rollno)
    print("Roll no: ", rollno,"\nName: ", name)
elif option == 1:
    enterData()