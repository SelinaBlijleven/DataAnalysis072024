"""
build_string.py

Contains basic examples around building up a string procedurally, as well as alternate approaches.
"""


def main():
    # We have some list of values that we want to use in the string_tasks.
    numbers: list = [0, 6, 5, 7, 3, 2, 6, 9, 0, 0]

    print(f"This demo contains some code that shows how you can build up a string.")
    print(f"We start with the following list: {numbers}")
    print(f"This number will be converted to a phone number string in two ways!")

    nr1 = build_string(numbers)
    nr2 = build_string_alt(numbers)

    print(f"Phone number, with numbers added element by element: {nr1}")
    print(f"Phone number, using the join() function: {nr2}")


def build_string(lst: list) -> str:
    """
    Build a string_tasks from a list

    This is the most common way to build up a string_tasks from elements of a list, although your
    exact approach may vary based on your goal.
    """
    string_number: str = ""

    # We can loop over the list with the enhanced for-loop
    for element in lst:
        # For every number, we convert it to a string, since they are numbers now!
        # In other cases, we might need to do some more preparation for these list items.
        # We can use the + symbol to add the string_tasks to what we already have.
        string_number += str(element)

    return string_number


def build_string_alt(lst: list):
    """
    Build a string_tasks from a list (alternate solution)

    This alternate trick allows us to join the elements of the list,
    using a specified string_tasks. Because that string_tasks is empty, we simply get the
    list of numbers back as a string_tasks.

    Smart use of functions and list comprehension sometimes allow us to get a lot done
    in a few lines of code. Using pre-defined functions can also speed up your program!

    We can even make this function a (slightly confusing) one-liner:
    `return "".join([str(element) for element in lst])`
    """
    # Make sure everything in the list is a string
    str_list = [str(element) for element in lst]
    return "".join(str_list)


if __name__ == "__main__":
    main()
