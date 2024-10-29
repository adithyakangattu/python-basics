#perform a case-insensitive sort of the list:

thislist = ["banana","Orange","Kiwi","cherry"]
thislist.sort(key = str. lower)

print(thislist)

#the key parameter is set to str.lower
#which means that the list will be sorted based
#on the lower case version of each string element

#"banana". lower ()returns "banana"#
#"Orange".lower()returns "Orange"
#"kiwi" . lower () returns "kiwi"
#"cherry".lower () returns "cherry"
