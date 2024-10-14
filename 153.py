#make a change in the original dictionary ,
# and see that the values list gets updated as well:

car = {
    "brand": "ford",
    "model": "miustang",
    "year": 1964

}
x = car.values()
print(x)  #before the change

car["year"] = 2020
print(x)   #after the change