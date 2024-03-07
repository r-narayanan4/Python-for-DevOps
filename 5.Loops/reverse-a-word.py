#  Python program to reverse a given text:

text = input("Enter a text: ")
reversed_text = ""
index = len(text) - 1

while index >= 0:
    reversed_text += text[index]
    index -= 1

print("Reversed text:", reversed_text)
