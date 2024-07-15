class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        """
        The string method (also called a dunder method), helps us
        represent objects as readable text.

        :return:    Human-readable person description
        """
        return f"{self.name}({self.age})"


class Auto:
    """ Class implementation """

    # This is not strictly necessary, but good practice!
    # It tells us which types we will be working with.
    brand: str
    build_year: int

    def __init__(self, brand, build_year):
        """
        Initialize the car

        :param brand:       We pass a brand for each car
        :param build_year:  We also pass a build year
        """
        self.brand = brand
        self.build_year = build_year

    def start(self) -> None:
        """
        This is a very simple function: it only prints some information
        using the car name. In a realistic scenario, this code would probably be replaced
        by the start-up logic for the car.

        :return:    This functions just prints, no return value
        """
        print(f"We starten de {self.brand}!")

    def __str__(self) -> str:
        """
        Return a human-readable string for the car.

        :return:    String representation of the car
        """
        return f"Auto is een {self.brand} uit {self.build_year}"

    def __eq__(self, other) -> bool:
        """
        Compare an Auto to any other object.

        :param other:
        :return:
        """
        if type(self) != type(other):
            return False

        return (self.brand, self.build_year) == (other.brand, other.build_year)


# Construct a person and two cars, this doesn't print anything
p1 = Person("John", 36)
auto1 = Auto("Mercedes", 2005)
auto2 = Auto("Opel", 2010)
auto3 = Auto("Opel", 2010)

# Now we can print our objects to learn more about them, using their __str__ functions.
print(str(p1))
print(str(auto1))       # the str() is implicit
print(auto2)            # so we don't have to use it

# Call an object method
auto2.start()

print(auto3 == auto2)
