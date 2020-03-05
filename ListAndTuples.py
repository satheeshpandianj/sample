import math
nameList = ["Satheesh","Praba","Adhira","Satheesh","Adhira","London"]
print(list("First time ")+ nameList)
print(set(nameList))
print(nameList)
print(nameList.count("Satheesh"))
nameList1 = nameList.copy()
print(nameList1)
nameList1.append("AdhiraPandian")
print(nameList1)
nameList.extend(nameList1)
print(nameList)
print(nameList.index("London",6,len(nameList)))
print(nameList)
nameList.insert(4,"Madhumitha")
print(nameList)
print(nameList.pop(1))
nameList.remove("Satheesh")
print(nameList)
del nameList[0]
print(nameList)
nameList.sort()
print(nameList)
nameList.reverse()
print(nameList)
nameList.sort(reverse=False)
print(nameList)
print(min(nameList))
print(nameList)
print(max(nameList))
print(nameList)
if("Swindon" not in nameList):
    print("its available")
else:
    print("its available")
#print(nameList + nameList)


