num = int(input("num="))
start = num
global adder

def loop_func(n):
    adder = 0
    for nums in range(start, 1):
        adder = adder + nums

    return adder

result = loop_func(num)
print(result)
