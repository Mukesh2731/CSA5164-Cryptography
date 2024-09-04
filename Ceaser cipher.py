# Input text from the user
text = input("Enter the text: ")

# Input shift amount from the user
shift = int(input("Enter shift amount: "))

# Choose operation from the user
choice = int(input("Choose operation (1 for Encrypt, 2 for Decrypt): "))

# Ensure shift is within 0-25
shift = shift % 26

# Initialize result variable
result = ""

# Process each character in the text
for char in text:
    if char.isalpha():  # Check if character is a letter
        base = 'A' if char.isupper() else 'a'
        # Encrypt or decrypt character based on the choice
        if choice == 1:  # Encrypt
            result += chr((ord(char) - ord(base) + shift) % 26 + ord(base))
        elif choice == 2:  # Decrypt
            result += chr((ord(char) - ord(base) - shift) % 26 + ord(base))
        else:
            result = "Invalid choice"
            break
    else:
        # Non-alphabetic characters remain unchanged
        result += char

# Output the result
print("Result:", result)
