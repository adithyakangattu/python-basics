# Add any iterable

#The object in the update() method does not have to be a set ,
# it can be any iterable object (tuples, lists, dictionaries etc.)


thisset = {"apple","banana","cherry"}              #set
mylist = ["kiwi","orange"]                         #list

thisset.update(mylist)

print(thisset)