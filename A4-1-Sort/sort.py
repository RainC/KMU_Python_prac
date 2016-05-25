#sort usage
friends = ["Alice","Carole","Bob"]
friends.sort()

friends.sort(reverse=True)

print(friends)



#Find the minimum number in array for bubble sort

a = [8,4,9,5]
small = a[0]
for i in range(1, len(a)):
	if small >= a[i]:
		small = a[i]
print(small) # 4

small = a[0]

for i in a:
	if small >= i:
		small = i

print(small) #4

# Find the Maxium number in array for bubble sort

maxs = 0
for i in a:
	if maxs <= i:
		maxs = i

print(maxs)

# Bubble Sort for non-Internal-function


list_numbers = [8,4,9,5]
count = 0
print("bubble")
for i in range(0, len(list_numbers) -1)
	if (list_numbers[count] <= list_numbers[count + 1]):
		list_numbers[count] = list_numbers[count + 1]
	count = count + 1
	print(count)


print(list_numbers)

