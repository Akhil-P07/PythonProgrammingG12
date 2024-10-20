f1 = open("Program10.txt")
f2 = open("Program10.txt","w")
for line in f1:
    if 'a' not in line:
        f2.write(line)
print("file copied successfully")
f1.close()
f2.close()