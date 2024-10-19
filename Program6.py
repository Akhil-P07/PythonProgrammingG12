import os
with open('Program6.txt', 'r') as file:
    for line in file:
        words = line.strip().split()
        print('#'.join(words))
