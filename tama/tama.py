

ehezes=0
cmd = ''
halal = False
while cmd != 'vege':	
	ehezes += 1
	if cmd == 'etet' :
		ehezes -= 7
	if ehezes > 7 :
		print('Éhezek!')
	cmd = input('Tama: ')
	if ehezes > 15:
		halal = True	
	if halal == True :
		print('Meghaltam')
		cmd = 'vege'
	




	


