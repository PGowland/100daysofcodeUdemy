#Write your code below this line 👇

def prime_checker(number):
  answer = False
  if number > 1:
    for i in range(2, number):
      if (number % i) == 0:
        answer = True
        break
  if answer:
    print(str(number) + " is not prime")
  else:
    print(str(number) + " is prime")
  
  




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



