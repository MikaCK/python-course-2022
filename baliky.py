baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}


kod_baliku = input('Kod baliku?')

print(kod_baliku)

if kod_baliku in baliky:
    print (f'Balík {baliky[kod_baliku]}')
    
else:
    print
