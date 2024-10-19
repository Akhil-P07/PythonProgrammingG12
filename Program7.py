#Program to read the content of file and display the total number of
#consonants, uppercase, vowels and lower case characters

file = open("Program7.txt", "r")
ncharacters = 0
nvowels = 0
nconsonants = 0
nupper = 0
nlower = 0

for line in file:
    print(line)
    for letter in line:
        if letter != " " and letter != "\n":
            print(letter)
            ncharacters += 1
        if letter.isupper():
            nupper += 1
        elif letter.islower():
            nlower += 1
    for vowels in ['a', 'e', 'i', 'o','u']:
        nvowels += line.count(vowels)

print("No. of vowels: ", nvowels)
nconsonants = ncharacters - nvowels
print("No. of consonants", nconsonants)
print("No. of Uppercase characters", nupper)
print("No. of Lowercase Characters", nlower)