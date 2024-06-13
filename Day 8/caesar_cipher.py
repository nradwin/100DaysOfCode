import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ''
  if cipher_direction == 'decode':
    shift_amount *= -1
  for char in start_text:
    # if the user enters a number/symbol/space
    if char not in alphabet:
      end_text += char
    else:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
  
  print(f'Here\'s the {cipher_direction}d result: {end_text}')
  
# ask the user if they want to restart the cipher program
task_complete = False
while not task_complete:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  # if user enters shift is greater than the number of letters in the alphabet
  if shift > 26:
    shift %= 26
  
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  
  restart = input('Would you like to encode/decode another message? y/n\n').lower()
  if restart == 'n':
    task_complete = True
    print('Thanks for using Ceasar Cipher. Have a blessed day.')