"""
functions_demo.py
"""


def optellen(a: int, b: int) -> int:
    return a + b


def statistiek(lijst: list) -> tuple[int, int]:
    gem = sum(lijst) / len(lijst)
    var = sum([(n - gem) ** 2 for n in lijst]) / len(lijst)
    return gem, var


# Opdracht: laat de gebruiker een getal invoeren en print of deze even of oneven is.

res = statistiek([5, 6, 2, 6, 8, 3, 3])
print(res)
print(list(res))
