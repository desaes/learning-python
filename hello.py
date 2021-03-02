print("hello")
nome = "Marcos Fontana"
print(nome.split()[0])
print(nome[0:6])

# listas
lista = [1, 2, 4, 7, "Marcos"]
lista.append("python")
print(lista)
lista.index(4) # search for 4 and return position
print(lista.count(3)) # count the number of occurances of 3 in the list
lista.remove("python")
lista.reverse()
print(lista)
lista2 = [8,3,56,7,2,34,6]
lista2.sort()
print(lista2)

# dicionarios
telefones = {"marcos": 993661011, "val": 991256282}
print(telefones)

# tuples are faster than lists and write protected
tuplas = ('marcos', 'val', 'davi')
print(tuplas)
print(tuplas[0:2])
print(len(tuplas)) # size
if (4 in tuplas):
    print("found")
else:
    print("not found")
tuplas2 = tuple(lista2)
print(tuplas2)

# for
for i in range(0,5):
  print(i)

nome="Marcos"
for letra in nome:
    print(letra)

for value in lista2:
    print(value) 

i=0
while(i < 10):
    print(i)
    i=i+1

i = 10
while True:
    i = i -1
    if (i == 4):
        continue
    print(i)
    if (i == 2):
        break

for x in range(0,5):
    pass # it's lile a comment, but it is not ignored... useful to use inside loops when you don't know the logic yet