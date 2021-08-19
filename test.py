test_str = "GeeksforGeeks"
res = ''.join(format(ord(i), '08b') for i in test_str)
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
digArr = []
a = []
last = ""
index = 0
aCount = 0
#aCount is for the 0's in bianary and bCount is for the 1's
bCount = 0
for i in res:
    a.append(i)
for i in a:
    digArr.append(int(i))
print("starting to print the string in bianary")
last = a[0]
finalArray = []
for i in digArr:
    if i == last and index > 0:
        if i == 0:
            aCount += 1
        if i == 1:
            bCount += 1
    elif index < 1:
        if i == 0:
            aCount += 1
        if i == 1:
            bCount += 1
    elif i == 0:
        finalArray.append(aCount)
    elif i == 1:
        finalArray.append(alphabet[index])
    index+=1    
    last = i
print(bCount)