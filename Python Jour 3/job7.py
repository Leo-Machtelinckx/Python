alphabet="abcdefghijklmnopqrstuvwxyz"*10
compteur=-1
for letter in alphabet:
    compteur+=2
    if compteur>27:
        break
    print(alphabet[0:compteur].center(27))