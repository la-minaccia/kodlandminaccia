import random

char = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
nchar = int(input("Inserisci il numero di caratteri della password"))


out = ""

for i in range(nchar):
    nout = random.randint(0, 72)
    out += char[nout]

print("password:", out)

