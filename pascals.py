b = int(input("Enter the number of rows: "))  # Number of rows
for i in range(b):  # Outer loop for rows
    print(" " * (b - i - 1), end="")  # Print leading spaces for formatting
    num = 1  # First number in every row is 1
    for j in range(i + 1):  # Inner loop for elements in the row
        print(num, end=" ")  # Print the current number
        num = num * (i - j) // (j + 1)  # Calculate the next number in the row
    print()  # Move to the next line after each row
 