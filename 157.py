# Add a new item to the original dictionary,
# and see that the items list gets updated as wll:


car = {
    "brand": "ford",
    "model": "mustang",
    "year": 1964

}
x = car.items()
print(x)   #before the change

car["color"] = "red"
print(x)   #after the change