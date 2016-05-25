#array management 
family = ["Mother","Father","Old Brother", "Brother"]
family.append("Me")
list_for_nummbers = [1,2,3,4,5,6]
print(family)
print(family[0])
print(list_for_nummbers[-1]) # last data of index print(6)


print("---------------------------------------------")
#slice list
mylist = ["string1","string2","string3","string4"]
print (mylist[0:1])

numbers = [1,2,3,4,5,6]
print(numbers[1:4])

print("---------------------------------------------")
#print the type of variable

int_numbers = [1,2,3,4,5,6]
string = ["dummy_data","Work"]
print("int_numbers of index 1 type : " , type(numbers[1]))
print("string variable type : " , type(string))# <class 'list'>
print("string variable index 3 type " , type(string[0]))# <class 'list'>

print("---------------------------------------------")
#list in list

int_data = [1,5,6,8,8,9]
str_data = ["abc","def","hij","klm"]
last_data = ["int_data", int_data , "str_data", str_data]
print(last_data)

print("---------------------------------------------")
#inssrt/delete item to index
list_data = ["a","b","c","d"]
list_data.append("e")
list_data.append("f")

list_data_2 = ["a","b","c","d","e"]
list_data_2.remove("c")
del list_data_2[1]
pop_x = list_data_2.pop()

print("list: " ,list_data)
print("pop : " , pop_x)

print("---------------------------------------------")
#search string in array

list_data_3 = ["a","b","c","d","e"]
print("b" in list_data_3) # return True : type Bool

if "a" in list_data_3:
	print("there is 'a'")
else:
	print("there is not 'a'")
	

print("---------------------------------------------")
#get index 
list_data_4 = ["MacBook","Windows","Apple","Samsung"]
print(list_data_4.index("Apple"))

print("---------------------------------------------")`
#range data in variable

numbers_range = list(range(100))
print(numbers_range)


print("---------------------------------------------")
#for each example (list)

string_data = ["a","b","c","d"]
for per_data in string_data:
	print(per_data)



