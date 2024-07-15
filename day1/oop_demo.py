class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name}({self.age})"


class Auto:
    brand: str
    build_year: int

    def __init__(self, brand, build_year):
        self.brand = brand
        self.build_year = build_year

    def start(self):
        print(f"We starten de {self.brand}!")

    def __str__(self) -> str:
        return f"Auto is een {self.brand} uit {self.build_year}"


p1 = Person("John", 36)
auto1 = Auto("Mercedes", 2005)
auto2 = Auto("Opel", 2010)

print(str(p1))
print(str(auto1))
print(str(auto2))
auto2.start()
