"""
optional_arguments.py

In Python, we can use optional arguments in our function definitions.
They use a default value if None is provided. This makes using the function
easier to use and helps us define standard behavior, while allowing us to
use the function in a more advanced way.

We will see this concept reoccur in Machine Learning a lot, where parameters
often have a sensible default built-in, making the libraries much more userfriendly.
"""


def hallo_functie(voornaam: str = "Pietje", achternaam: str = "Programmeur"):
    print(f"Hallo! Mijn voornaam is {voornaam} en mijn achternaam is {achternaam}")


hallo_functie(voornaam="Jurre", achternaam="Brandsen")
hallo_functie()
