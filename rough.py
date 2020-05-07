def maxFreq(l):
    # Please add your code here
    my_dict = {}
    for e in l:
        my_dict[e] = my_dict.get(e, 0) + 1
    # print(my_dict)
    max_val = 0
    max_key = None
    for e in my_dict:
        if my_dict[e] > max_val:
            max_val = my_dict[e]
            max_key = e
    return max_key


# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
print(maxFreq(l))
