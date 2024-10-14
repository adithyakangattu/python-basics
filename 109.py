#using asterisk*

#If the number of variables is less than the number of values
#you can add a * to the variable name
#And the values will be assigned to the variable as a list

#Assign the rest of the values as a list called "red":

fruits = ("apple","banana","cherry","strawberry","raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)