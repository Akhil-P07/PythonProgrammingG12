x = int(input("Enter num: "))
a = list()
for i in range(1, x + 1):
  if(x % i == 0):
    a.append(i)
print(a)
if len(a) == 0 or len(a) == 1:
  print(x, "is not a prime number.")
elif a[0] == 1 and a[1] == x:
  print(x, "is a prime number.")
else:
  print(x, "is not a prime number.")