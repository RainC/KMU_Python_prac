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

    
# input num:17
# center: 8
#                                      i/desc/cent/plus/init
# ********+********                                    0 False 8 1 False
# *******+++*******                                    1 False 7 3 True
# ******+++++******                                    2 False 6 5 True
# *****+++++++*****                                    3 False 5 7 True
# ****+++++++++****                                    4 False 4 9 True
# ***+++++++++++***                                    5 False 3 11 True
# **+++++++++++++**                                    6 False 2 13 True
# *+++++++++++++++*                                    7 False 1 15 True
# +++++++++++++++++                                    8 False 0 17 True
# *+++++++++++++++*                                    9 True 1 15 True
# **+++++++++++++**                                    10 True 2 13 True
# ***+++++++++++***                                    11 True 3 11 True
# ****+++++++++****                                    12 True 4 9 True
# *****+++++++*****                                    13 True 5 7 True
# ******+++++******                                    14 True 6 5 True
# *******+++*******                                    15 True 7 3 True
# ********+********                                    16 True 8 1 True