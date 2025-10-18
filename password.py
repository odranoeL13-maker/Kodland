import random

#  variabili
simboli = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890([])"

quantita = int(input("quanti simboli vuoi?"))

password = ""


for i in range(quantita):
    password += random.choice(simboli)
if quantita <= 5:
    print("ma è troppo facile indovinarla")
elif quantita >= 10:
    print("ma come farai a ricordarla?")
else:    
    print("ecco la tua password:", password)
