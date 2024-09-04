import string

# User input
key = input("Enter a key (unique letters for the cipher): ").lower()
text = input("Enter the text: ").lower()
mode = input("Do you want to 'encrypt' or 'decrypt'?: ").strip().lower()

# Generate a cipher alphabet based on the provided key
key = ''.join(sorted(set(key), key=key.index))  # Remove duplicates, maintain order
alphabet = string.ascii_lowercase
cipher_alphabet = key + ''.join([c for c in alphabet if c not in key])

# Set up the translation table
if mode == 'decrypt':
    cipher_alphabet, alphabet = alphabet, cipher_alphabet

translation_table = str.maketrans(alphabet, cipher_alphabet)

# Perform encryption or decryption
result = []
for char in text:
    if char in alphabet:
        result.append(char.translate(translation_table))
    else:
        result.append(char)  # Non-alphabet characters remain unchanged

# Output the result
print(f"Result: {''.join(result)}")
