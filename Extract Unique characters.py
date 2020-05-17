def uniqueChars(string):
    lst = list(string)
    if len(lst) == 0:
        return
    my_dict = {}
    for e in lst:
        my_dict[e] = my_dict.get(e, 0) + 1
    # print(my_dict.items())
    for e in lst:
        if e in my_dict:
            print(e, end="")
            del my_dict[e]

# Main
string = input()
uniqueChars(string)
