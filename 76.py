#Return "orange" instead of "banana" ?


fruits = ["apple","banana","cherry","kiwi","banana"]

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
