# write a program to replace items with a given value if exists in a list?
original_list = [1, 2, 3, 4, 2, 5, 2, 6]

# Values to Replace
target_value = 2
replacement_value = 99

# Replace items in the list
modified_list = [replacement_value if item == target_value else item for item in original_list]

# Display the Lists
print(f"Original List: {original_list}")
print(f"Modified List: {modified_list}")
