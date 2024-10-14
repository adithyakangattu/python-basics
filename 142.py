#you can use the ^ operator
#instead of the symmetric_difference () method .
# and you will get the same result .


#use ^ to join two sets ?

set1 = {"apple","banana","cherry"}
set2 = {"google","insta","apple"}

set3 = set1 ^ set2
print(set3)

#the ^ operator only allows you to join sets with sets .
# and not with the other data types
# like you can with the symmetric_difference () method .