def busBin(lista):
    op=0
    buscar=int(input("Ingrese el numero: "))
    low=0
    high=len(lista)-1
    while True:
        op+=1
        mid=(high+low)//2
        if mid+1==high:
            if buscar == lista[high]:
                print(f"Encontrado op={op}")
                break
            else:
                print(f"No encontrado op={op}")
                break
        elif buscar<lista[mid]:
            high=mid
        elif buscar>lista[mid]:
            low=mid
        elif buscar==lista[mid]:
            print(f"Encontrado op={op}")
            break
numeros=[2,5,10,15,20,25,30,35,40,45,50,58,65,80,98]
busBin(numeros)

