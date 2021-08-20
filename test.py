test_str = input("Enter message:")
res = ''.join(format(ord(i), '08b') for i in test_str)
alphabet = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
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
last = digArr[0]
finalArray = []
if last == 0:
    aCount += 1
elif last == 1:
    bCount += 1
size = len(digArr)
for i in digArr:
    
    if index > 0:
        if i == 1:
            bCount += 1
            if i != last:
                finalArray.append(aCount)
                aCount = 0
        if i == 0:
            aCount += 1
            if i != last:
                finalArray.append(alphabet[bCount  - 1])
                bCount = 0
    last = i
    index+=1

if bCount > 0:
    finalArray.append(alphabet[bCount - 1])
    bCount = 0
if aCount > 0:
    finalArray.append(aCount)
    aCount = 0
stringversion = ""
for i in finalArray:
	stringversion+=str(i)
print(stringversion)
