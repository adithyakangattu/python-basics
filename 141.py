#Symmetric differences

#the symmetric_difference () will keep only
# the elements that are NOT present in both sets.

#keep the items that are not present in both sets ?

set1 = {"apple","banana","cherry"}
set2 = {"google","insta","apple"}

set3 = set1.symmetric_difference(set2)
print(set3)