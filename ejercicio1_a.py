#1.a
lista = [2,20,3,4,5,6,7,8,9,19,11,12,13,14,17,16,15,18,10,1]
i=0
j=0
aux=0
tam=len(lista)
while i<tam-1:
	j=0
	while j<tam-1:
		if lista[j+1]<lista[j]:
			aux=lista[j+1]
			lista[j+1]=lista[j]
			lista[j]=aux
		j=j+1
	i=i+1
else:
	print lista