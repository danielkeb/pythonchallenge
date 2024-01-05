# Read numbers from file1.txt
with open('file1.txt', 'r') as file1:
    num1 = [line.strip() for line in file1.readlines()]

# Read numbers from file2.txt
with open('file2.txt', 'r') as file2:
    num2 = [line.strip() for line in file2.readlines()]

    # Find common numbers
    result = [com for com in num2 if com in num1]

# Print the results
print("Numbers from file1:", num1)
print("Numbers from file2:", num2)
print("Common Numbers:", result)
