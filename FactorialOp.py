a = int(input("Enter for factorial: ")) #Factorial of number
b = 1
if a == 0:
    print(str(a) + "! =", 1)
else: 
    for i in range(1, a + 1):
        b *= i
    print(str(a)  + "! =", b)