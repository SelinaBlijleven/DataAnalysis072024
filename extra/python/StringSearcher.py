import os


def search(fname, targetlen: int):
    # Read the file to search
    with open(fname, "r") as file:
        data = file.read().split()

    # Search with
    return [d for d in data if len(d) == targetlen]


if __name__ == "__main__":
    print(search(os.getcwd() + "/potential_passwords.txt", 5))
