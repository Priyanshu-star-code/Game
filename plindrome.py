#   Write a program to print whether the string is symmetrical or palindrome.
string=input("Enter your string \n")
cleaned_string = string.replace(" ", "").lower()
# Check if the cleaned string is equal to its reverse
if cleaned_string == cleaned_string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
