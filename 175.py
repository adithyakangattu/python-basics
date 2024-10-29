#loop through nested dictionaries

#you can loop through a dictionary
# by using the items() method like this .

#loop through the keys and values of all nested dictionaries ?

myfamily = {
    "child1": {
        "name":"emil",
        "year": 2004
},
   "child2": {
       "name": "tobias",
       "year": 2007
},
    "child3": {
        "name": "lins",
        "year": 2011
    }
}
for x , z in myfamily.items():
    print(x)
    for y in z:
        print(y + ':', z[y])