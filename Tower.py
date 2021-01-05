def hanoi(n,A,B,C):
    if n == 1:
        print("Move sheet {} from {} to {}".format(n,A,C))

    else:
        hanoi(n-1,A,C,B)
        print("Move sheet {} from {} to {}".format(n,A,C))
        hanoi(n-1,B,A,C,)
hanoi(3,'第一个','第二个','第三个')