def pairSum0(l):
    si = 0
    ei = len(l)-1
    for i in range(0, ei):
        for j in range(i+1, ei+1):
            if l[i] == -l[j]:
                print(min(l[i], l[j]), end=" ")
                print(max(l[i], l[j]))

def pair_sum1(l):
    my_dict = {}
    for e in l:
        if -e in my_dict:
            print(min(e, -e), end=" ")
            print(max(e, -e))
        my_dict[e] = my_dict.get(e, 0) + 1

n=int(input())
l=list(int(i) for i in input().strip().split(' '))
pair_sum1(l)