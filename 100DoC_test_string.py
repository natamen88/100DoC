letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

word = ""

for char in letters:
    word += char

print("This is the string created from a list and using 'for': " + word)

word2 = "".join(letters)

print("This is the string created from a list and using the 'join' function: " + word2)


