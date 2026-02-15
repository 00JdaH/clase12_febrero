def intercambioPosicione(lista):
    primero=lista[-1]
    ultimo=lista[0]
    lista[0]=primero
    lista[-1]=ultimo
       
    return lista












corredores=[]
tam = int(input("ingrese el numero de corredores: "))
for i in range(tam):
    corredor = input(f"ingrese el corredor #{i+1}: ")
    corredores.append(corredor)
    
lista=intercambioPosicione(corredores)
print(lista)