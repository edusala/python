# Sallai András, 2020-10-15, esti Szoft
print('Sallai András, 2020-10-15, esti Szoft')
print('A Feladat 0411 megoldása')

valos1 = 35.38
valos2 = 83.23
valos3 = 211.05

if valos2 < valos1 and valos3 < valos1:
	print(valos1)
elif valos1 < valos2 and valos3 < valos2:
	print(valos2)
elif valos1 < valos3 and valos2 < valos3:
	print(valos3)
else:
	print('egyik sem teljesült')

