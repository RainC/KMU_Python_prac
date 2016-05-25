def get_index(y,m,d):
    strs = str(y)
    left_y = int(strs[0:2])
    right_y = int(strs[2:4])
    month= int(m)
    day = int(d)
    calc = (21 * left_y) + (5 * right_y / 4) + ((26* month) + (26 * 1)) / 10 + day -1
    print(int(calc % 7))
    
    #return int((21 * left_y) + (5 * right_y / 4) + 26 (m + 1) / 10 + d -1 % 7)
    


#index_list = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat",]
#print(index_list[get_index(2015,12,9)])
print(get_index(2016,12,12))
