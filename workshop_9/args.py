# print(5, 7, 7, 5, 4, 3, 2, 1, 2, 3, 4, 5, sep="", end="|\n\n\n\n\n")

def create_list(a, b, *args, k=17, **kwargs):
    print(type(kwargs), kwargs)
    return list(args)
    # lst = []
    # for element in args:
    #     lst.append(element)
    # # print(type(args), args)
    # return lst


# data = create_list(1, 2, "hello", True, [1, 2, 3])
data = create_list(1, 6, 6, 7, 8, c=7, luka=16, k=-111)
data = create_list(9, 10)

print(data, type(data))