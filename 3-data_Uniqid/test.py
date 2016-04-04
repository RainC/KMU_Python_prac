#Python Memory Address 
alphapet = ["a","b","c","d","z","s","r","q"]
myAlpha = alphapet

print(id(alphapet) , id(myAlpha))

alphapet.sort()
print(id(alphapet) , id(myAlpha))

print("--------------------------------")
#deep copy
alphapet_list = ["a","b","c","d","e","z","g","w"]
alphapet_copy = alphapet[:]

print(id(alphapet), id(alphapet_copy))
alphapet_list.sort()
