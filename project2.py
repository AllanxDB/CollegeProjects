
# Ask the user for input
text = input("Enter a sentence: ")

# Count how many vowels and consonants are in the string
vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for ch in text.lower():  # element-level: work with each character
    if ch.isalpha():
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1


# Split the text into words (list) and count how many times each appears (dictionary)
words = text.split()
word_count = {}

for word in words:
    # Remove punctuation at the end of the word
    word = word.strip(".,!?")
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# conditional logic
if vowel_count > consonant_count:
    message = "Your sentence has more vowels than consonants."
elif consonant_count > vowel_count:
    message = "Your sentence has more consonants than vowels."
else:
    message = "Your sentence has an equal number of vowels and consonants!"

# output results

print("Total words:", len(words))
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
print(message)
print("Word frequencies:")
for word, count in word_count.items():
    print(f"  {word}: {count}")