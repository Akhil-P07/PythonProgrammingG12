import pickle
data = dict()
def updateMarks(rollNo):
    file = open("Program8.txt", "rb")
    data = pickle.load(file)
    for key in data:
        value = data.get(key)
        if value[0] == rollNo:
            return value[1]  
    return -1

def enterData():
    file = open("Program8.txt", 'wb')
    n  = int(input("Enter no. of entries: "))
    for i in range(n):
        rollNo = int(input("Enter roll no. "))
        name = input("Enter name: ")
        marks = input("Enter marks: ")
        data["Student entry #%i"%(i + 1)] = [rollNo, name, marks]
    pickle.dump(data, file)
    file.close()

option = int(input("Would you like to:\n1. Update marks - Press 0\n2. Enter data - Press 1\nChoose: "))

if option == 0:
    rollno = int(input("Enter roll no: "))
    name = seekData(rollno)
    if name != -1:
        print("Roll no: ", rollno,"\nName: ", name)
    else:
        print("Rollno not found")
elif option == 1:
    enterData()