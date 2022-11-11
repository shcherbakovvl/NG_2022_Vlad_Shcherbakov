def findingFrequences():   #Function that count every letter
    for i in editedString:
        if i in frequence:
            frequence[i] += 1
        else:
            frequence[i] = 1


print ("======================================")
rawString = str(input("Hello, I can sort your words or sentences by number of letters :3\nType something: "))   #initialising string
editedString = rawString.replace(" ", "")   #deleting all spaces
frequence = {}   #initialising dict
findingFrequences()   #initialising our function
sortedFrequence = sorted(frequence.items(), key = lambda x:x[1], reverse = True)   #sorting by using .sorted
print ("======================================")
print ("Counted letters:\n", str(frequence), "\nSorted:\n", sortedFrequence)
print ("======================================")