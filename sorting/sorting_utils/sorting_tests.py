from sorting.sorting_utils.random_list_generator import non_unique_1d as randlst


def test_sorts(sorts):
    # Create random nums, and valid sort
    nums = randlst()
    valid = sorted(nums)
    print(f"Given: {nums}", f"Sorted: {valid}", sep="\n", end="\n\n")

    # Sort the nums
    for (func_name, sort) in sorts.items():
        result = sort(nums.copy())
        print(f">>> {func_name}: {result}", f"{result == valid}", sep=" | ")


if __name__ == "__main__":
    test_sorts({"Built-in Sort": sorted})
