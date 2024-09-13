# Function to reverse the letters in a word using a for loop
def reverse_word(word):
    reversed_word = ""
    # Iterate through the word in reverse order
    for i in range(len(word) - 1, -1, -1):
        reversed_word += word[i]
    return reversed_word

# Example usagej
original_word = "vall"
reversed_word = reverse_word(original_word)
print("Original word:", original_word)
print("Reversed word:", reversed_word)