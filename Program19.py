import mysql.connector as mycon

con = mycon.connect(host='127.0.0.1', user='root', password="admin", database="company")
cur = con.cursor()

print("#" * 40)
print("EMPLOYEE UPDATION FORM")
print("#" * 40)
print("\n\n")

ans = 'y'
while ans.lower() == 'y':
    eno = int(input("ENTER EMPNO TO UPDATE: "))
    query = "SELECT * FROM employee WHERE empno={}".format(eno)
    cur.execute(query)
    result = cur.fetchall()
    
    if cur.rowcount == 0:
        print("Sorry! Empno not found.")
    else:
        print("%10s" % "EMPNO", "%20s" % "NAME", "%15s" % "DEPARTMENT", "%10s" % "SALARY")
        for row in result:
            print("%10s" % row[0], "%20s" % row[1], "%15s" % row[2], "%10s" % row[3])
        
        choice = input("\n## ARE YOU SURE TO UPDATE? (Y): ")
        if choice.lower() == 'y':
            print("== YOU CAN UPDATE ONLY DEPT AND SALARY ==")
            print("== FOR EMPNO AND NAME CONTACT ADMIN ==")
            d = input("ENTER NEW DEPARTMENT (LEAVE BLANK IF NOT WANT TO CHANGE): ")

            if d == "":
                d = row[2]
            
            try:
                s = int(input("ENTER NEW SALARY (LEAVE BLANK IF NOT WANT TO CHANGE): "))
            except:
                s = row[3]
            
            query = "UPDATE employee SET dept='{}', salary={} WHERE empno={}".format(d, s, eno)
            cur.execute(query)
            con.commit()
            print("## RECORD UPDATED ##")

    ans = input("UPDATE MORE (Y): ")
