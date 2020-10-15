# Szövegkezelés
# benev.py

nev = input('Név: ')
nev = nev.rstrip()

if nev == 'János':
	print('Üdv János')

# Minden white spacer karaktert
# töröl jobbról
# szóköz, tabulátor, sorvége, 
# vízszintes tabulátor

# Darabolás
dolgozo = 'Nagy János;Szolnok;3840000;38'
#print(type(dolgozo))

tomb = dolgozo.split(';')
print(tomb[2])
#print(dolgozo[2])

szoveg='valami'
hossz=len(szoveg)
for i in range(1, hossz):
    print(szoveg[i-1], '-')
  
