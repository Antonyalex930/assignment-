
a = input("Enter : ")

unique = []

for i in a:
    if i not in unique:
        unique.append(i)
def listToString(str):
    str1 = ""
    for ele in str:
        str1 += ( ele + ",")
    return str1
str = unique
print(listToString(str).rstrip(","))
