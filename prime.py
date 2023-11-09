#   Write a program to display all prime numbers within a range.
num=int(input("Enter your range number\n "))
num1=int(input("Enter your range number1 \n "))
print ("The Prime Numbers in the range are: ")  
for number in range (num, num1+ 1):  
    if number > 1:    # check greater than 1
        for i in range (2, number):  
            if (number % i) == 0:  #checks if the current number is divisible by i
                break  
        else:  
            print (number)