txt = input("Enter text to search: ")
word = input("Enter word that has to be searched for: ")
a = txt.count(word)
if a > 1:
    print(word, "is found %i times in the text"%(a))
elif a == 1: 
    print(word, "is found %i time in the text"%(a))
else: print(word, "is not found in the text")