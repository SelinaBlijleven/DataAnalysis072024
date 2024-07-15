a: range = range(10)
b: range = range(0, 10)
c: range = range(0, 10, 1)

# Different ways to print the same:
print(a)
print(b)
print(c)

# Iterate over a range
# Enhanced for-loop
for number in a:
    print(number)

# Traditional for loop:
# for(i = 0 ; i < len(a) ; i++)

no_list: list = []

# Python equivalent
for i in range(len(a)):
    no_list.append(i)

print(f"The range(10) results in list {no_list}")

# With list comprehension we can do this in one line
print(f"The range(0, 10) results in list {[number for number in b]}")
