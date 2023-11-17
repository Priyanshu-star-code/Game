#   Find the length of the string avoiding spaces from the string?
string = "Hello, world! How are you doing?"

#  replace(" ", "") method is used to replace all spaces with an empty string
string2 = string.replace(" ","")

# Find the length of the string without spaces
length = len(string2)

print("Original string:", string)
print("String without spaces:", string2)
print("Length without spaces:", length)