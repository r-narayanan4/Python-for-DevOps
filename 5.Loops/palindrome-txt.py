text = input("Enter a text: ")
original_text = text
reverse_text = ""

# Reversing the text
for char in text:
    reverse_text = char + reverse_text

# Checking if the original text is equal to the reversed text
if original_text == reverse_text:
    print("Palindrome!")
else:
    print("Not a Palindrome!")
