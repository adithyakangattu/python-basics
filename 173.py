# create three dictionaries
# then create one dictionary that will contain
# the other three dictionaries ?

child1 = {
    "name": "Tobias",
    "year": 2004
}
child2 = {
    "name": "Emil",
    "year": 2007
}
child3 = {
    "namw": "linvs",
    "year": 2011
}

myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
print(myfamily)