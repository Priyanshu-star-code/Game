#  Calculate the sum of all digits in a user-defined number?
num=int(input("Enter any number "))
# Initialize a variable to store the sum of digits
sum = 0
# using while loop 
while(num>0):
    # using modules operater 
    sum=sum+num%10 
    num=num//10
print("Here sum of digit ", sum)   