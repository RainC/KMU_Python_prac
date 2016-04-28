dic = {2015123:"Alice", 2015200: "bob", "KMU" : "JeongReung"}
print("keys : " ,dic.keys())


#Find all dictionary
dic = {2015123: "Alice" , 2015200: "bob", "kmu" : "jeongreung"}

for key in dic:
	print(key, "'s value is " , dic[key])

print()

for key, value in dic.items();
	print(key, "'s value is " , value)

# 리스트와 딕셔너리 차이점 
# 리스트 : 입력된 순서가 유지됨 
# 인덱스를 통한 접근

# Dictionaries
# 정해진 순서가 없음
# 키를 통한 접근
