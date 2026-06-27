import time
import random

opciones = ["piedra","tijera","papel"]
x = len(opciones)
victoria_usuario = 0
victoria_maquina = 0

while victoria_usuario < 3 and victoria_maquina < 3:
  user = input("Escoge entre piedra papel o tijera")
  maquina = random.choice(opciones)
  
  if user not in opciones:
    print("Opcion no valida!")
    continue
  
  if maquina == user:
    print("Empate")
    continue
  
  if user == "tijera":
    if maquina == "papel":
      print("El usuario gano!")
      victoria_usuario = victoria_usuario + 1
      continue
    
    print("El usuario perdio")
    victoria_maquina= victoria_maquina +1
  
  
  
  if user == "piedra":
    if maquina == "tijera":
      print("El usuario gano!")
      victoria_usuario = victoria_usuario + 1
      continue
    
    print("El usuario perdio")
    victoria_maquina= victoria_maquina +1

   

  if user == "papel":
    if maquina == "piedra":
      print("El usuario gano!")
      victoria_usuario = victoria_usuario + 1
      continue
    
    print("El usuario perdio")
    victoria_maquina= victoria_maquina +1
    

if victoria_usuario > victoria_maquina:
  print("El usuario gano el juego final")
else:
  print("El usuario perdio el juego final.")
  
print("Usuario: " + str(victoria_usuario) + " Maquina: " + str(victoria_maquina))
