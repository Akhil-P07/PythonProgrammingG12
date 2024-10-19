#Prints the fibonacci sequence until the last set number eg. 0,1,1,2,3,5,8,13
nth = int(input("Enter the required no. of term in the fibonacci sequence: "))
if nth < 1:
    print("Input must be a Natural number.")
    quit()
a = 0
b = 1
seq=list()
for i in range(nth):
    seq.append(a)
    seq.append(b)
    a += b
    b += a
print(seq)
print(seq[nth - 1])
