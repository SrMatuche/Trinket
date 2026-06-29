import random

random_number = random.randint(1, 100)
intentos = 0

while True:
    intentos = intentos + 1
    guess = input("que numero crees que es")
    
    if not guess.isnumeric():
      print("solo numeros" )
      continue
    
    guess = int(guess)
    
    if guess == random_number:
      print("felicidades adivinaste")
      break
    elif guess > random_number:
      print("Tu numero es muy grande")
    else:
      print("Tu numero es muy pequeño")
      
print("Te tomo " + str(intentos) + " intentos")
