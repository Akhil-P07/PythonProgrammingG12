import mysql.connector as mycon

con = mycon.connect(host='127.0.0.1', user='root', password="admin", database="company")
cur = con.cursor()

print("#" * 40)
print("EMPLOYEE SEARCHING FORM")
print("#" * 40)
print("\n\n")

ans = 'y'
while ans.lower() == 'y':
    eno = int(input("ENTER EMPNO TO SEARCH: "))
    query = "SELECT * FROM employee WHERE empno={}".format(eno)
    cur.execute(query)
    result = cur.fetchall()
    
    if cur.rowcount == 0:
        print("Sorry! Empno not found.")
    else:
        print("%10s" % "EMPNO", "%20s" % "NAME", "%15s" % "DEPARTMENT", "%10s" % "SALARY")
        for row in result:
            print("%10s" % row[0], "%20s" % row[1], "%15s" % row[2], "%10s" % row[3])
    
    ans = input("SEARCH MORE (Y): ")
