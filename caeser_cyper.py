alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = list(input("Type your message:\n").lower())
shift = int(input("Type the shift number:\n"))
answer = []


def caeser(direction, text, shift):
  if direction == 'encode':
    for letter in text:
      if letter in alphabet:
        answer.append(alphabet[(alphabet.index(letter)+shift)%26])
      else:
        answer.append(letter)
    encrypted_message = "".join(answer)  
    print("Your encrypted message is " + encrypted_message)
  else:
    for letter in text:
      if letter in alphabet:
        answer.append(alphabet[(alphabet.index(letter)+shift)%26])
      else:
        answer.append(letter)
    encrypted_message = "".join(answer)  
    print("Your encrypted message is " + encrypted_message)
  

 
caeser(direction=direction, text=text, shift=shift)
