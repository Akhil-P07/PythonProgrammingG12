#Example list of first 10 numbers
l = list(range(11))
i = 0
sum = 0
def f(x):
    global sum, i
    sum += x[i]
    i += 1
    if i == len(x):
        return sum
    return f(x)
print(f(l))