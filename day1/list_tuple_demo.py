"""
list_tuple_demo.py

A simple demo illustrating the capabilities of lists vs. tuples.
"""


def list_overview():
    print("List Overview")
    # Creating a list
    my_list = [1, 2, 3, 4, 5]
    print(f"List: {my_list}")

    # Appending to the end of the list
    my_list.append(6)
    print(f"After append: {my_list}")

    # Removing an element from a list by value
    my_list.remove(2)
    print(f"After remove: {my_list}")

    # Setting a new value for a list element
    my_list[0] = 10
    print(f"After modification: {my_list}")

    # List slicing
    print(f"Sliced list: {my_list[1:4]}")

    # Other useful list methods
    print(f"Length of list: {len(my_list)}")
    print(f"Index of 4: {my_list.index(4)}")
    print(f"Count of 3: {my_list.count(3)}")


def tuple_overview():
    print("\nTuple Overview")
    # Creating a tuple
    my_tuple = (1, 2, 3, 4, 5)
    print(f"Tuple: {my_tuple}")

    # Basic operations (Note: Tuples are immutable)
    # (We are creating an error on purpose)
    try:
        my_tuple[0] = 10
    except TypeError as e:
        print(f"Error: {e}")

    # Tuple slicing
    print(f"Sliced tuple: {my_tuple[1:4]}")

    # Tuple methods
    print(f"Length of tuple: {len(my_tuple)}")
    print(f"Index of 4: {my_tuple.index(4)}")
    print(f"Count of 3: {my_tuple.count(3)}")


def main():
    # Run the two functions
    list_overview()
    tuple_overview()


# Make sure we only execute code if this is the entry point :)
if __name__ == "__main__":
    main()
