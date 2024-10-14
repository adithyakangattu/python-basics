#update tuples

#change tuple values
#once a tuple is crated, you cannot change its values,
#tuple are unchangeable , or immutable as it also is called.

#you can convert the tuple in to list
#change the list and convert the list back in to tuple

#convert the tuple into a list to be able to change it ?

x = ("apple","banana","cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
