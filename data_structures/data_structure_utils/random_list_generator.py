dft = [10, 10, 100, 10]  # dft = default (range, low, high, row)

## Non-unique random list (1d, 2d)
from random import randrange


def non_unique_1d(info=dft[:-1]):
    r, low, high = info  # r: range
    return [randrange(low, high) for num in range(r)]


def non_unique_2d(info=dft):
    *info_1d, rows = info
    return [non_unique_1d(info_1d) for i in range(rows)]


# Unique random list (1d, 2d)
from random import sample


def unique_1d(info=dft[:-1]):
    r, low, high = info  # r: range
    return sample(range(low, high), r)  # unique sample


def unique_2d(info=dft):
    *info_1d, rows = info
    return [unique_1d(info_1d) for i in range(rows)]


## Test
# rdict = {"non_unique_1d": non_unique_1d,
#          "non_unique_2d": non_unique_2d,
#          "unique_1d": unique_1d,
#          "unique_2d": unique_2d,}

# cases = {"1d": [5, 15, 25], "2d": [8, 11, 30, 5]}
# def rdict_test():
#     c1d, c2d = cases.values() # get test cases
#     for name, func in rdict.items(): # loop thru the functions
#         print(f"{name} -----------------------------------------")
#         if "1d" in name:
#             print(f"default: {func()}",
#                   f"rand: {func(c1d)}", sep = "\n")
#         elif "2d" in name:
#             print(f"default:")
#             for row in func():
#                 print(row)

#             print(f"rand:")
#             for row in func(c2d):
#                 print(row)
#         print()

# rdict_test()
