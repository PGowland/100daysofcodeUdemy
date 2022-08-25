alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = list(input("Type your message:\n").lower())
shift = int(input("Type the shift number:\n"))
answer = []


def caeser(direction, text, shift):
  if direction == 'decode':
    shift *= -1
  for letter in text:
    if letter in alphabet:
      answer.append(alphabet[(alphabet.index(letter)+shift)%26])
    else:
      answer.append(letter)
  complete_message = "".join(answer)  
  print("Your message is " + complete_message)
  
caeser(direction=direction, text=text, shift=shift)
  

