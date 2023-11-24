# Two lists of numbers
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

# Create a new list with odd numbers from list1 and even numbers from list2
new_list = [num for num in list1 if num % 2 != 0] + [num for num in list2 if num % 2 == 0]

# Display the result
print("List 1:", list1)
print("List 2:", list2)
print("New List:", new_list)
