test_str = "a"
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
print(digArr)
print("starting to print the string in bianary")
last = a[0]
finalArray = []
for i in digArr:
    if index > 0:
        if i == last:
            if i == 0:
                aCount += 1
            if i == 1:
                bCount += 1
        elif i is not last:
            if i == 0:
                aCount += 1     
                finalArray.append(aCount)
                aCount = 0
            if i == 1:
                bCount += 1
                finalArray.append(alphabet[bCount])
                bCount = 0
    elif index < 1:
        if i == 0:
            aCount += 1
        if i == 1:
            bCount += 1
    index+=1    
    last = i
if bCount > 0:
    finalArray.append(aCount)
if aCount > 0:
    finalArray.append(alphabet[bCount])
aCount = 0
bCount = 0
finalArray.pop(0)
lastOne = []
for i in finalArray:
    if i is not 0:
        lastOne.append(i)
print(lastOne)