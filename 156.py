# Make a change in the original dictionary,
#  and see that the items list gets updated as well:

car = {
    "brand": "ford",
    "model": "mustang",
    "year": 1964
}
x = car.items()
print(x) #before the change

car["year"] = 2020
print(x) #after the change