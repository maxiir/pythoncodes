def listpares (limite):
	
	num=1
	milist=[]
	
	while num<limite:
		
		milist.append(num*2)
		num=num+1
	
	return milist

print(listpares(99))