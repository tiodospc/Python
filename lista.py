#UMA NOVA LISTA:  Brit prog dos anos 70
a = 1
b = 2
c = 3
d = 4
progs = [a, b, c, d]

#FOR PARA VARER A LISTA

for progs in progs:
    print (progs)
    
#trocando o ultimo elemento
f= 42
progs[-1] = f
print (progs)

#incluindo
g= 23
progs.append (g)
print(progs)

#removendo
progs.remove(c)
print (progs)

#ordena a lista
progs.sort()
print (progs)

#inverte a lista
progs.reverse()
print(progs)

#imprime enumerado
for i in enumerate(progs):
    print (i+1,'=>',progs)

#imprime do 2 item em diante
print (progs[1:])
