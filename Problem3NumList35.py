#by Medina Kubanychbekova
#03/11/2025

# Problem 3: Asking user for numbers until sum exceeds 100
num_list = []  # Initialize an empty list
sum_of_numbers = 0  # Track sum of entered numbers

while sum_of_numbers <= 100:
    num = int(input("Enter a number: "))  # Get user input
    num_list.append(num)  # Append number to list
    sum_of_numbers += num  # Update sum

print("Final list of numbers:", num_list)
print("Sum of numbers:", sum_of_numbers)
