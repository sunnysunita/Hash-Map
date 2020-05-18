
def printPairDiffK(lst, k):
    my_dict = {}
    for e in lst:
        my_dict[e] = my_dict.get(e, 0) + 1
    # print(my_dict.items())
    for e in lst:
        if my_dict[e] > 0:
            my_dict[e] = my_dict[e] - 1

            if e-k in my_dict and my_dict[e-k] != 0:
                for i in range(my_dict[e-k]):
                    print(e, e-k)

            if k != 0 and e+k in my_dict and my_dict[e+k] != 0:
                for i in range(my_dict[e+k]):
                    print(e, e+k)



n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
printPairDiffK(lst, k)