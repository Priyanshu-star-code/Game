from collections import Counter
# Write a program to print the maximum frequency character in a given string?
# take user input 
string = input("enter string ")
# Split the input string into words
words = string.split()
# word cout git 
count_words = Counter(words)
# use max function
max_word = max(count_words, key=count_words.get)
print("Maximun frequency in the string ", max_word )
