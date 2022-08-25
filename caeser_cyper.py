alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = list(input("Type your message:\n").lower())
shift = int(input("Type the shift number:\n"))
answer = []
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):
  for letter in text:
    if letter in alphabet:
      answer.append(alphabet[(alphabet.index(letter)+shift)%26])
    else:
      answer.append(letter)
  encrypted_message = "".join(answer)  
  print("Your encrypted message is " + encrypted_message)

def decrypt(text, shift):
  for letter in text:
    if letter in alphabet:
      answer.append(alphabet[(alphabet.index(letter)-shift)%26])
    else:
      answer.append(letter)
  decrypted_message = "".join(answer)
  print("Your decrypted message is " + decrypted_message)
    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
if direction == 'encode':
 encrypt(text=text, shift=shift)
else:
  decrypt(text=text, shift=shift)
