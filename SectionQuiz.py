# Question 1: Create a for loop that counts from 0 to 10, and prints odd numbers to the screen.

print("Question 1:")

for i in range(1, 11):
    if i % 2 != 0:
        print(i)

# Question 2: Create a while loop that counts from 0 to 10, and prints odd numbers to the screen.

print()  # Empty line for better readability
print("Question 2:")

count = 0
while count <= 10:
    if count % 2 != 0:
        print(count)
    count += 1

# Question 3: Create a program with a for loop and a break statement.
# The program should iterate over characters in an email address,
# exit the loop when it reaches the @ symbol, and print the part before @ on one line.

print()  # Empty line for better readability
print("Question 3:")

for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")

# Question 4: Create a program with a for loop and a continue statement.
# The program should iterate over a string of digits, replace each 0 with x,
# and print the modified string to the screen.

print()  # Empty line for better readability
print()  # Empty line for better readability
print("Question 4:")

for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")

# Question 5: What is the output of the following code?

# n = 3

# while n > 0:
#    print(n + 1)
#    n -= 1
# else:
#    print(n)

print()  # Empty line for better readability
print()  # Empty line for better readability

print("Question 5:")
print("The output of the code will be: ")
print("4")
print("3")
print("2")
print("0")

# Question 6: What is the output of the following code?

# n = range(4)

# for num in n:
#    print(num - 1)
# else:
#    print(num)

print()  # Empty line for better readability
print()  # Empty line for better readability

print("Question 6:")
print("The output of the code will be: ")
print("-1")
print("0")
print("1")
print("2")

# Question 7: What is the output of the following code?

# for i in range(0, 6, 3):
#    print(i)

print()  # Empty line for better readability
print()  # Empty line for better readability

print("Question 7:")
print("The output of the code will be: ")
print("0")
print("3")
