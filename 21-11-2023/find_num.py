'''  write a Python program to find numbers between 300 and 800 (both included )
where each digit of a number is an even number.explain ''' 
# Find numbers between 300 and 800 with all even digits
numbers = [num for num in range(300, 500)if all(int(digit) % 2 == 0 for digit in str(num))]
# Display the result
print(f"Numbers between 300 and 800 with all even digits:\n", numbers)
