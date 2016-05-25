def hanoi(n, from_, to_,with_):
    if n > 0:
        hanoi(n - 1, from_, with_, to_)
        print("move " ,n , "from ",from_, "to ", to_)
        hanoi( n-1, with_, to_, from_)


n_diskc = 3
t1 = 1
t2 = 2
t3 = 3

hanoi(3,1,3,2)

