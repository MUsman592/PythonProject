# Question 1
"""
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
num4 = int(input("Enter the fourth number: "))
num5 = int(input("Enter the fifth number: "))

largest = second_largest = float('-inf')   

for num in [num1, num2, num3, num4, num5]:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num


print("The second largest number is:", second_largest)

"""
# Question2

num = input("Enter up to 8 numbers separated by spaces: ")

# Split input into a list
numbers = num.split()

# Check the number of entered values
if len(numbers) > 8:
    print("Error: You entered more than 8 numbers!")
elif len(numbers) < 8:
    print("Error: You entered less than 8 numbers!")
else:
    # Convert each value to an integer
    numbers = [int(num) for num in numbers]
    print("Your 8 numbers are:", numbers)
    
    print("\nYour 8 numbers are:", numbers)
    print("\nFrequency of each number:")

    # Count occurrences of each number
    for num in set(numbers):
        print(f"{num} appears {numbers.count(num)} time(s)")