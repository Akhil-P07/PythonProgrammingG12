import mysql.connector as mycon

con = mycon.connect(host='127.0.0.1', user='root', password="admin")
cur = con.cursor()
cur.execute("CREATE DATABASE IF NOT EXISTS company")
cur.execute("USE company")
cur.execute("CREATE TABLE IF NOT EXISTS employee(empno INT, name VARCHAR(20), dept VARCHAR(20), salary INT)")
con.commit()

choice = None
while choice != 0:
    print("1. ADD RECORD ")
    print("2. DISPLAY RECORD ")
    print("0. EXIT")
    choice = int(input("Enter Choice: "))
    
    if choice == 1:
        e = int(input("Enter Employee Number: "))
        n = input("Enter Name: ")
        d = input("Enter Department: ")
        s = int(input("Enter Salary: "))
        query = "INSERT INTO employee VALUES({}, '{}', '{}', {})".format(e, n, d, s)
        cur.execute(query)
        con.commit()
        print("## Data Saved ##")
    
    elif choice == 2:
        query = "SELECT * FROM employee"
        cur.execute(query)
        result = cur.fetchall()
        
        print("%10s" % "EMPNO", "%20s" % "NAME", "%15s" % "DEPARTMENT", "%10s" % "SALARY")
        for row in result:
            print("%10s" % row[0], "%20s" % row[1], "%15s" % row[2], "%10s" % row[3])
    
    elif choice == 0:
        con.close()
        print("## Bye!! ##")
    
    else:
        print("## INVALID CHOICE ##")
