
from Cliente import*
from Funciones import*
import numpy as np



arreglo = np.full((10,10),'---')


ciclo= True
llenar(arreglo)
num_asiento=0
while (ciclo):
    print("Menu Creativos.cl")
    print("1) Comprar Asiento")
    print("2) Ubicaciones disponibles")
    print("3) Ver listado de asistentes")
    print("4) Mostrar totales")
    print("5) Salir")
    try:
        op=int(input("Seleccione 1-5:"))
        match op:
            case 1:
                print("COMPRAR")
                comprarAsiento(arreglo,num_asiento)
            case 2:
                print("Ubicaciones dispo")
                mostrar(arreglo)
            case 3:
                print("listado")
                listaClientes(lista_clientes)
            case 4:
                print("Total")
                totales(lista_clientes)
            case 5:
                ciclo = salir()
    except BaseException as error:
        print(f"error:{error}")
