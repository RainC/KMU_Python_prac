import pickle

f = open("test.dat", "wb")
lst = ["sdfdsf", "sdfdsfdsfasdfawefawef", 60, 3.14512343214134132]
pickle.dump(lst, f)

new_list = pickle.load(f)

print(new_list)
f.close()

