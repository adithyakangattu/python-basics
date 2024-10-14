#remove items
#note: you cannot remove items in a tuple

#Tuples are unchangeable , so you cannot items from it ,
# but you can use the same workaround as we used for changing
#and adding tuple items:

#convert tuple in to a list , remove "apple"
# and convert it back into a tuple ?


thistuple = ("apple","banana","cheery")
y = list (thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)