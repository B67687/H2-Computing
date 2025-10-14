from sorting.sorting_utils.randlst_gen import non_unique_1d, non_unique_2d, unique_1d, unique_2d

RANDOM_GENERATOR_1D = (
    non_unique_1d,
    unique_1d,
)

RANDOM_GENERATOR_2D = (
    non_unique_2d,
    unique_2d,
)

RANDOM_GENERATORS = (
    *RANDOM_GENERATOR_1D,
    *RANDOM_GENERATOR_2D,
)

CASES = {
    "1d": (5, 15, 25),
    "2d": (8, 11, 30, 5),
}


def print_matrix(matrix):
    "Prints out the matrix in a pretty way, a simple implementation"
    for row in matrix:
        print(row)


def test_random_generators():
    """Prints out the default and custom 1-dimentional and 2-dimentional lists."""

    arguments_1d, arguments_2d = CASES.values()

    for func in RANDOM_GENERATORS:
        name = func.__name__
        default_random_nums = func()

        print()
        print("---------------------")
        print(f">>> {name}")
        print("---------------------")

        print()
        if "1d" in name:
            print("Default:")
            print(default_random_nums)
            print()
            print("Custom:")
            print(func(arguments_1d))

        elif "2d" in name:
            print("Default:")
            print_matrix(default_random_nums)
            print()
            print("Custom:")
            print_matrix(func(arguments_2d))

        print()


if __name__ == "__main__":
    test_random_generators()
