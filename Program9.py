import pickle
student=[]
f=open('student.dat','wb')
ans='y'
while ans.lower()=='y':
    roll = int(input("Enter Roll Number :"))
    name = input("Enter Name :")
    marks = int(input("Enter Marks :"))
    student.append([roll,name,marks])
    ans=input("Add More ?(Y)")
pickle.dump(student,f)
f.close()
f=open('student.dat','rb+')
student=[]
while True:
    try:
        student = pickle.load(f)
    except EOFError:
        break

ans='y'

while ans.lower()=='y':
    found=False
    r = int(input("Enter Roll number to update :"))
    for s in student:
        if s[0]==r:
            print("## Name is :",s[1], " ##")
            print("## Current Marks is :",s[2], " ##")
            m = int(input("Enter new marks :"))
            s[2]=m
            print("## Record Updated ##")
            found=True
            break
    if not found:
        print("####Sorry! Roll number not found ####")
    ans=input("Update more ?(Y) :")
f.close()