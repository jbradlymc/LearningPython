secret_word = "chupacabra"
guess = ""

while guess != secret_word:
    guess = input("Enter the secret word: ")
    if guess == secret_word:
        break
print("You've successfully left the loop.")
