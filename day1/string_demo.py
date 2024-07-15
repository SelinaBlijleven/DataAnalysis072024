text1: str = "Hello World, how are you doing?"
text2: str = "I hope today will be a good day.        "

print(f"Text2 is: {text2} with length {len(text2)}")

# Remove whitespace
text2 = text2.strip()
print(f"Text2 is: {text2} after stripping, with length {len(text2)}")

# Formatting string in Python
print(f"{text1} {text2}")

# Lowercase text
print(f"{text1.lower()}")
print(f"{text1[::-1]}")


