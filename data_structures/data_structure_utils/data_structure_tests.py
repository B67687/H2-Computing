from data_structure_utils.random_list_generator import unique_1d as randlst
from random import randint, sample


# >>> Test for Members (Attributes and Methods) --------------------------------------------------------------
def members_check(initialised_data_structure, expected_attrs: tuple, expected_methods: tuple):

    for attr in expected_attrs:
        if not hasattr(initialised_data_structure, attr):
            print(f"Missing Attribute in Initialisation: {attr}")
            return False
                
    for method in expected_methods:
        if not callable(getattr(initialised_data_structure, method)):
            print(f"Missing Method in Class: {method}")
            return False

    return True


# >>> Linked List --------------------------------------------------------------------------------------------

        
def LinearLinkedList_Test(LinearLinkedList):
    # Create random lists
    r = randint(15, 18)
    test = randlst([r, 10, 100])
    a, b = len(test) // 3, -3
    notinlst, inlst, after_empty_test = test[:a], test[a:b], test[b:]
    print(
        f"test: {test}",
        f"notinlst: {notinlst}",
        f"inlst: {inlst}",
        f"after_empty_test: {after_empty_test}",
        sep="\n",
        end="\n\n",
    )

    # Create empty LLL
    LLL = LinearLinkedList()
    
    # Exit early if class member requirements not met
    expected_attrs = ("head", "size")
    expected_methods = (
        "empty", "insert", "sort_it", "delete",
        "search", "size_of", "display"
    )
    if not members_check(LLL, expected_attrs, expected_methods):
        return
        
    print(">>> LLL -------------------------------------------------------------------------------------")

    # Put items from inlst into LLL, and sort LLL
    for num in inlst:
        LLL.insert(num)

    if hasattr(LLL, "sort_it"):
        LLL.sort_it()

    ## Placeholder Line for Linear Singly Linked Lis
    def placeholder(truth_value: bool):
        truth_length = len(str(truth_value))
        
        print(
            f"Size: {LLL.size_of()}",
            f"Data (  ): {' ':{truth_length}}",
            f"    ",
            f"LLL: {LLL.display()}",
            sep=" | ",
            end="",
        )
    placeholder(False)
    
    ## Postpend truthiness of display function
    print(f" | Display: {LLL.display() == sorted(inlst)}")
    print() 
    
    ## Test notinlst
    print("Pop Out Not In List -------------------------------------------------------------------------------------")
    for num in notinlst:
        print(
            f"Size: {LLL.size_of()}",
            f"Data ({num}): {LLL.search(num)}",
            f"{LLL.delete(num)}",
            f"LLL: {LLL.display()}",
            sep=" | ",
        )
    print()

    # Test inlst
    print("Pop Out In List -------------------------------------------------------------------------------------")

    placeholder(True)
    print()
    
    for num in inlst:
        print(
            f"Size: {LLL.size_of()}",
            f"Data ({num}): {LLL.search(num)}",
            f"{LLL.delete(num)}",
            f"LLL: {LLL.display()}",
            sep=" | ",
        )
    print()

    # Test after_empty_test
    print("Empty -------------------------------------------------------------------------------------")
    for num in after_empty_test:
        print(
            f"Size: {LLL.size_of()}",
            f"Data ({num}): {LLL.search(num)}",
            f"{LLL.delete(num)}",
            f"LLL: {LLL.display()}",
            sep=" | ",
        )


# >>> Stack --------------------------------------------------------------------------------------------------

def Stack_Test(Stack):
    # Create random list
    lst = randlst()
    print(f"List: {lst}", end="\n\n")

    # Create Empty Stack
    S = Stack()

    # Exit early if class member requirements not met
    expected_attrs = ("_stack",)
    expected_methods = (
        "push", "pop", "peek", "size",
        "display",
    )
    
    if not members_check(S, expected_attrs, expected_methods):
        return

    # Display characteristics of the class
    print(">>> Stack:")
    print(
        f"Stack: {S.display()}",
        f"Size: {S.size()}",
        f"Top: {S.peek()}",
        sep=" | ",
        end="\n\n",
    )

    # Put items into stack
    for item in lst:
        S.push(item)
    print(f"Top: {S.peek()}", f"Stack: {S.display()}", sep=" | ", end="\n\n")

    # Remove items from stack
    for _ in range(len(lst)):
        print(
            f"Popped: {S.pop()}",
            f"Top: {S.peek()}",
            f"Size: {S.size()}",
            f"Stack: {S.display()}",
            sep=" | ",
        )


# >>> Queue --------------------------------------------------------------------------------------------------

# Linear
def LinearQueue_Test(LinearQueue):
    # Create random list
    lst = randlst()
    print(f"List: {lst}")

    # Create Empty LQ
    LQ = LinearQueue()

    # Exit early if class member requirements not met
    expected_attrs = ("_queue",)
    expected_methods = (
        "enqueue", "dequeue", "peek", "size",
        "display",
    )
    
    if not members_check(LQ, expected_attrs, expected_methods):
        return

    # Display characteristics of the class
    print(">>> LQ:")
    print(
        f"LQ: {LQ.display()}",
        f"Size: {LQ.size()}",
        f"Front: {LQ.peek()}",
        sep=" | ",
        end="\n\n",
    )
    
    # Put items into LQ
    for item in lst:
        LQ.enqueue(item)
    print(f"Front: {LQ.peek()}", f"LQ: {LQ.display()}", sep=" | ", end="\n\n")

    # Remove items from LQ
    for _ in range(len(lst)):
        print(
            f"Deq: {LQ.dequeue()}",
            f"Front: {LQ.peek()}",
            f"Size: {LQ.size()}",
            f"LQ: {LQ.display()}",
            sep=" | ",
        )


# Circular
def CircularQueue_Test(CircularQueue):
    # Create random list
    nums = randlst()
    print(f"List: {nums}", sep=" | ", end="\n\n")

    # Create Empty CQ with length less than lst
    len_CQ = len(nums) - 1
    try:
        CQ = CircularQueue(len_CQ)
    except TypeError:
        print("Missing Attribute required for Initialisation: _max_size")
        return
        
    # Exit early if class member requirements not met
    expected_attrs = ("_queue", "_max_size", "_size", "_head")
    expected_methods = (
        "empty", "full", "update_tail", "update_head",
        "enqueue", "dequeue", "head_at", "head_at", "tail_at",
        "max_size_of", "size_of", "display",
    )
    
    if not members_check(CQ, expected_attrs, expected_methods):
        return

    # Display characteristics of the class
    print(">>> CQ")
    print(f"Max_size: {CQ.max_size_of()}")
    print()

    # Headers and ALignment
    temp_headers = ["Status", "Size", "Head", "Tail", "Circular Queue"]
    headers = " | ".join(temp_headers)
    align_data = [len(_) for _ in temp_headers]

    # General display format
    def display(status):
        # Display data
        temp_display_data = [
            status,
            CQ.size_of(),
            CQ.head_at(),
            CQ.tail_at(),
            CQ.display(),
        ]
        display_data = [str(_) for _ in temp_display_data]

        # Make the headers / data on one line
        temp_line_data = []
        for display, align in zip(display_data, align_data):
            centered_display = display.center(align)
            temp_line_data.append(centered_display)
        line_data = " | ".join(temp_line_data)
        return line_data

    # Start
    print("---START", headers, sep="\n")
    print(display(CQ.dequeue()))
    print()

    # Fill CQ completely
    print("---ENQUEUE", headers, sep="\n")
    for num in nums:
        print(display(CQ.enqueue(num)))
    print()

    # Remove half of CQ
    mid = len_CQ // 2
    print("---DEQUEUE", headers, sep="\n")
    for _ in range(mid):
        print(display(CQ.dequeue()))
    print()

    # Fill CQ back to full
    print("---ENQUEUE", headers, sep="\n")
    for i in range(mid, len_CQ):
        print(display(CQ.enqueue(nums[i])))
    print()

    # Remove all in CQ
    print("---DEQUEUE", headers, sep="\n")
    for _ in range(len_CQ):
        print(display(CQ.dequeue()))
    print()

    # End
    print("---END", headers, sep="\n")
    print(display(CQ.dequeue()))


# >>> Binary Search Tree -------------------------------------------------------------------------------------

def BinarySearchTree_Test(BinarySearchTree):
    # Create random list
    r = randint(5, 10)
    lst = randlst([r, 10, 100])
    print(f"List: {lst}", f"Sorted: {sorted(lst)}", sep="\n", end="\n\n")

    # Create empty BST
    BST = BinarySearchTree()
    
    # Exit early if class member requirements not met
    expected_attrs = ("root",)
    expected_methods = (
        "put", "find", "min_of", "max_of",
        "size", "height", "in_order", "pre_order", "post_order",
    )
    
    if not members_check(BST, expected_attrs, expected_methods):
        return

    print(">>> BST:")

    # Put items into bst
    for item in lst:
        BST.put(item)
    print(
        "AFTER INSERTION:",
        f"Size: {BST.size()} | {BST.size() == len(lst)}",
        f"Height: {BST.height()} | idk how to display this",
        f"Min: {BST.min_of()} | {BST.min_of() == min(lst)}",
        f"Max: {BST.max_of()} | {BST.max_of() == max(lst)}",
        sep="\n",
        end="\n\n",
    )

    items = sample(lst, 5) + randlst(
        [5, 10, 100]
    )  # 5 confirm in list, 5 might be in list
    found = [BST.find(_) for _ in items]
    zipped = list(zip(items, found))
    inlst, notinlst = zipped[:5], zipped[5:]
    print(
        f"Sampled from lst: {inlst} | {all(found[:5])}",
        f"Random: {notinlst}",
        sep="\n",
        end="\n\n",
    )
    lst.sort()
    print(
        f"Inord: {BST.in_order()} | {lst == BST.in_order()}",
        f"Preord: {BST.pre_order()}",
        f"Postord: {BST.post_order()}",
        sep="\n",
    )
