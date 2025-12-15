secret_number = 777

print(
    """
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

# Function to safely read an integer


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter an integer.")


guess_number = get_int("> ")

while guess_number != secret_number:
    print("Ha ha! You're stuck in my loop!")
    guess_number = get_int("> ")

print("Well done, muggle! You are free now.")
