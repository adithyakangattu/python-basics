#update dictionary
#the update() method will update the dictionary
# with the items from the given argument

# the argument must ba a dictionary ,
# or an iterable object with key:value paris.
#update the year of the car by using the update ()method :

thisdict = {
    "brand": "ford",
    "model": "mustang",
    "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)