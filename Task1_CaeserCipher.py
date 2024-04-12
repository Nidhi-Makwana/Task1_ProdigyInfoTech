alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def caesar_cipher(text, shift, mode):
 
  result = ""
  for letter in text:
    if letter.isalpha():
      new_index = (alphabets.find(letter.upper()) + shift) % 26
      new_letter = alphabets[new_index]
      result += new_letter if letter.isupper() else new_letter.lower()
    else:
      result += letter
  return result

# Get user input
text = input("Enter your message: ")
shift = int(input("Enter the shift value (positive for encryption, negative for decryption): "))
mode = input("Enter 'encrypt' or 'decrypt': ").lower()

# Check for valid mode
if mode not in ("encrypt", "decrypt"):
  print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")
  exit()

# Perform encryption or decryption
if mode == "encrypt":
  encrypted_text = caesar_cipher(text, shift, mode)
  print("Encrypted message:", encrypted_text)
else:
  decrypted_text = caesar_cipher(text, shift, mode)
  print("Decrypted message:", decrypted_text)
