#Access items in nested dictionary

#print the name of child2 ?

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
print(myfamily["child2"]["name"])