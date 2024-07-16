"""
input_validation.py

This file contains two input validation examples:

1. Example 1 will show you how to get confirmation from a user before proceeding.
2. Example 2 will allow the user to specify whether they want to receive a newsletter or not.
"""
from typing import Optional

# Keep a list of affirmative and negative words our users can use to answer.
AFFIRMATIVE = ["y", "yes"]
NEGATIVE = ["n", "no"]


def main() -> None:
    # Make the user agree to the terms and conditions
    input_validation()

    # Ask the user whether they want to subscribe to the newspaper.
    subscribe: bool = subscribe_newspaper()

    # Print some confirmation for the user
    text = f"Thank you for completing this form! You have accepted the terms and conditions."
    if subscribe:
        text += "You have also indicated that you would like to receive our newsletter."
    else:
        text += "You have indicated that you do not want to receive our newsletter."
    print(text)


def input_validation() -> None:
    """
    An example of a function that repeatedly asks for input,
    until correct input is given.

    :return:    given answer
    """
    # We will use this variable to check if we have a valid answer
    answer: str = ""

    # Iterate until we have set a valid answer
    while answer == "":
        # Ask the user
        consent: str = input("Do you agree to the terms and conditions? Y/N \n")

        # If the user answered y or Y, they consented and the program can move on
        # We use lower() to ignore capital letters.
        if consent.lower() in AFFIRMATIVE:
            # We have a valid answer from the user, next iteration the loop will stop
            answer = consent
        else:
            # Print some help for the user
            print("You can't use this program without agreeing!")

    # In this case, we don't have to update any databases, or pass data back,
    # so we do not use a return statement.


def subscribe_newspaper() -> Optional[bool]:
    """ Ask the user if they wish to subscribe to the newspaper. """
    # Store the answer later
    ans: Optional[bool] = None

    # Ask again until we have a clear yes or no
    while ans is None:
        sub: str = input("Do you want to subscribe to our newsletter? Y/N \n")

        # Check if we have an answer we can accept: we
        # combine both the yes and no answers.
        if sub.lower() in AFFIRMATIVE + NEGATIVE:
            # If the answer is valid, we need to determine if it is negative or affirmative
            ans = True if sub.lower() in AFFIRMATIVE else False

    # Now we return ans, which should contain either True or False at this point
    return ans


if __name__ == "__main__":
    main()
