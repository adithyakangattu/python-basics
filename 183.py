#print "vowel" if the character is a vowel ( a, e ,i ,o,u ) ,
#print "consonant" if the character is a consonant (any other alphabetical character)
#print "not an alphabet" if the charecter






char = "u"
print("vowel" if char.lower() in 'aeiou' else "consonant" if char.isalpha() else "not an alphabet")


