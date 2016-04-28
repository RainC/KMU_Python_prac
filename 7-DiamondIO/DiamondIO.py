k = int(input("input num:"))
num_center_set = int(k/2)
num_center = int(k/2)
num_plus_count = 1
DecreaseMode = False
InitProcess = False
print("center:", num_center)
print("\t\t\t\t\t\t\t\t\t i/desc/cent/plus/init")
for i in range(0, k):

    if (InitProcess == True):
        if (i == num_center_set + 1):
            DecreaseMode = True

        if DecreaseMode == True:
            num_center = num_center + 1
            num_plus_count = num_plus_count - 2
            
        if DecreaseMode == False:
            num_center = num_center - 1
            num_plus_count = num_plus_count + 2
            

        
    for j in range(0, k - num_plus_count + 1):
        if (num_center == j):
            for sp in range(0, num_plus_count):
                print("+" ,end="")
        else:
            print("*", end="")
    print("\t\t\t\t\t\t\t\t\t",i, DecreaseMode, num_center, num_plus_count, InitProcess)
    
    InitProcess = True
    
    
    
