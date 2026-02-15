
    
def segundaPosicionListaS(arreglo):
    tamaLista= len(arreglo)
    if tamaLista<2:
      return "none"
    else:
       return arreglo[1]
    

arreglo=[]
tam = int(input("ingrese el tamaño de la lista: "))

for i in range(tam):
    num = input(f"ingrese el elemento{i+1}: ")
    arreglo.append(num)


numerosegundo=segundaPosicionListaS(arreglo)
print(numerosegundo)
