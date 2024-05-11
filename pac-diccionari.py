## PAC - diccionari
## -------------------- IMPORTS  --------------------
from cowsay import cowsay
import os
import time

## -------------------- VARIABLES -------------------

diccionari = {}

## -------------------- FUNCIONS --------------------

def menuInicial():
    print(cowsay("----- Benvingut al diccionari -----\n"))
    print("1) Afegir una paraula/entrada")
    print("2) Mostrar una paraula/entrada")
    print("3) Modificar una paraula/entrada")
    print("4) Eliminar una paraula/entrada")
    print("5) Sortir")

def opcioValida(min,max):
    opcio = -1
    while opcio<min or opcio>max:
        opcio = input("\nSelecciona una opcio: ")
        opcio = int(opcio)
    return opcio

def afegirParEnt():
    os.system("cls")
    print(cowsay("----- Afegir una paraula o entrada -----\n"))
    print("1) Afegir una paraula")
    print("2) Afegir una entrada")
    opcio = opcioValida(1,2)
    if(opcio==1):
        print("\n----- Afegir una paraula -----\n")
        paraula = input("Escriu la paraula:")
        clau = input("Escriu la entrada:")
        valor = input("Descripció de l'entrada:")
        entrada = ({clau:valor})
        diccionari.update({paraula:entrada})
        neteja(1);
    if(opcio==2):
        print("\n----- Afegir una entrada -----\n")
        if diccionari == {}:
            print("No hi ha paraules al diccionari")
            neteja(2);
        else:
            print("Sobre quina paraula vols afegir una entrada\n")
            i = 0
            for key in diccionari:
                i += 1
                print(str(i) + ") " + key)
            numParaula = opcioValida(1,i)
            i = 1
            for key in diccionari:
                if (i == numParaula):
                    paraula = key
                    break
                i += 1
            auxiliar = diccionari[paraula]
            clau = input("\nEscriu la entrada:")
            valor = input("Descripció de l'entrada:")
            entrada = ({clau:valor})
            auxiliar.update(entrada)
            neteja(1);

def mostrarParEnt():
    os.system("cls")
    print(cowsay("---- Mostrar una paraula o entrada ----"))
    print("1) Mostrar una paraula")
    print("2) Mostrar una entrada")
    opcio = opcioValida(1,2)
    if(opcio==1):
        print("\n----- Mostrar una paraula -----\n")
        if diccionari == {}:
            print("No hi ha paraules al diccionari")
            neteja(2);
        else:
            i = 0
            for key in diccionari:
                i += 1
                print(str(i) + ") " + key)
            numParaula = opcioValida(1,i)
            i = 1
            for key in diccionari:
                if (i == numParaula):
                    paraula = key
                    break
                i += 1
            print(diccionari[paraula])
            neteja(1);
    if(opcio==2):
        print("\n----- Mostrar una entrada -----\n")
        if diccionari == {}:
            print("No hi ha paraules al diccionari")
            neteja(2);
        else:
            print("Sobre quina paraula vols mostrar una entrada\n")
            i = 0
            for key in diccionari:
                i += 1
                print(str(i) + ") " + key)
            numParaula = opcioValida(1,i)
            i = 1
            for key in diccionari:
                if (i == numParaula):
                    paraula = key
                    break
                i += 1
            auxiliar = diccionari[paraula]
            print("\nQuina entrada vols mostrar\n")
            i = 0
            for key in auxiliar:
                i += 1
                print(str(i) + ") " + key)
            numParaula = opcioValida(1,i)
            i = 1
            for key in auxiliar:
                if (i == numParaula):
                    paraula = key
                    break
                i += 1
            print(auxiliar[paraula])
            neteja(1);

def modificarParEnt():
    os.system("cls")
    print(cowsay("--- Modificar una paraula o entrada ---\n"))
    print("1) Modificar una paraula")
    print("2) Modificar una entrada")
    opcio = opcioValida(1,2)
    if(opcio==1):
        print("\n----- Modificar una paraula -----\n")
        if diccionari == {}:
            print("No hi ha paraules al diccionari")
            neteja(2);
        else:
            i = 0
            for key in diccionari:
                i += 1
                print(str(i) + ") " + key)
            numParaula = opcioValida(1,i)
            i = 1
            for key in diccionari:
                if (i == numParaula):
                    paraula = key
                    break
                i += 1
            novaParaula = input("\nEscriu la nova paraula:")
            auxiliar = diccionari[paraula]
            diccionari.update({novaParaula:auxiliar})
            diccionari.pop(paraula)
            neteja(1);
    if(opcio==2):
        print("\n----- Modificar una entrada -----\n")
        if diccionari == {}:
            print("No hi ha paraules al diccionari")
            neteja(2);
        else:
            print("Sobre quina paraula vols modificar una entrada\n")
            i = 0
            for key in diccionari:
                i += 1
                print(str(i) + ") " + key)
            numParaula = opcioValida(1,i)
            i = 1
            for key in diccionari:
                if (i == numParaula):
                    paraula = key
                    break
                i += 1
            auxiliar = diccionari[paraula]
            print("\nQuina entrada vols modificar\n")
            i = 0
            for key in auxiliar:
                i += 1
                print(str(i) + ") " + key)
            numParaula = opcioValida(1,i)
            i = 1
            for key in auxiliar:
                if (i == numParaula):
                    paraula = key
                    break
                i += 1
            auxiliar2 = auxiliar[paraula]
            auxiliar.pop(paraula)
            novaEntrada = input("\nEscriu la nova entrada:")
            novaDesc = input("Escriu la nova descripció:")
            auxiliar.update({novaEntrada:novaDesc})
            neteja(1);

def eliminarParEnt():
    os.system("cls")
    print(cowsay("----- Eliminar paraula o entrada -----\n"))
    print("1) Eliminar una paraula")
    print("2) Eliminar una entrada")
    opcio = opcioValida(1,2)
    if(opcio==1):
        print("\n----- Eliminar una paraula -----\n")
        if diccionari == {}:
            print("No hi ha paraules al diccionari")
            neteja(2);
        else:
            i = 0
            for key in diccionari:
                i += 1
                print(str(i) + ") " + key)
            numParaula = opcioValida(1,i)
            i = 1
            for key in diccionari:
                if (i == numParaula):
                    paraula = key
                    break
                i += 1
            diccionari.pop(paraula)
            neteja(1);
    if(opcio==2):
        print("\n----- Eliminar una entrada -----\n")
        if diccionari == {}:
            print("No hi ha paraules al diccionari")
            neteja(2);
        else:
            print("Sobre quina paraula vols eliminar les entrades\n")
            i = 0
            for key in diccionari:
                i += 1
                print(str(i) + ") " + key)
            numParaula = opcioValida(1,i)
            i = 1
            for key in diccionari:
                if (i == numParaula):
                    paraula = key
                    break
                i += 1
            auxiliar = diccionari[paraula]
            print("\nQuina entrada vols eliminar\n")
            i = 0
            for key in auxiliar:
                i += 1
                print(str(i) + ") " + key)
            numParaula = opcioValida(1,i)
            i = 1
            for key in auxiliar:
                if (i == numParaula):
                    paraula = key
                    break
                i += 1
            auxiliar.pop(paraula)
            neteja(1);

def sortir():
    print("\nEl joc es tancarà en 3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    os.system("cls")
    
def neteja(num):
    time.sleep(num)
    os.system("cls")

## ------------------ CODI DEL JOC ------------------

sortida = 0

while sortida == 0:
    print(diccionari)
    menuInicial();
    opcio = opcioValida(1,5)
    if (opcio==1):
        afegirParEnt();
    if (opcio==2):
        mostrarParEnt();
    if (opcio==3):
        modificarParEnt();
    if (opcio==4):
        eliminarParEnt();
    if (opcio==5):
        sortir();
        sortida = 1