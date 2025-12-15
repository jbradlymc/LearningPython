user_word = input("Please enter a word: ")
user_word = user_word.upper()

word_without_vowels = ""

for letter in user_word:
    if letter in "AEIOU":
        continue
    word_without_vowels += letter

print(word_without_vowels)
