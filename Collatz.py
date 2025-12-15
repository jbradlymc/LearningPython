steps = 0

while True:
    try:
        c0 = int(input("Enter a non-negative and non-zero integer number: "))
        if c0 > 0:
            break
        else:
            print("Invalid input. Please try again.")
    except ValueError:
        print("Invalid input. Please try again.")

while c0 != 1:
    if c0 % 2 == 0:
        c0 //= 2
    else:
        c0 = 3 * c0 + 1
    steps += 1
    print(c0)

print(f"steps = {steps}")
