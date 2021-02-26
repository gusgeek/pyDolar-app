#!/usr/bin/python
import requests
import os

def bancoGalicia():
    r = requests.get('https://www.bancogalicia.com/cotizacion/cotizar?currencyId=02&quoteType=SU&quoteId=999')
    jsonResponse = r.json()

    for key, value in jsonResponse.items():

        if key == 'error':
            print('Disculpe pero en este momento no es posible conseguir la cotizacion \nIntente nuevamente mas tarde')
        else:
            if key == 'buy':
                print(f'        Dolar Compra es de {value}')

            elif key == 'sell':
                print(f'        Dolar Venta es de {value}')

def DolarSI():
    r = requests.get('https://www.dolarsi.com/api/api.php?type=cotizador')
    jsonResponse = r.json()
    for data in jsonResponse:

        compra = data['casa']['compra']
        venta = data['casa']['venta']
        nombre = data['casa']['nombre']

        print(f"\n *** {nombre} ***")
        print(f" COMPRA {compra} - VENTA {venta}\n")

def AmbitoFinanciero():
    V = requests.get('https://mercados.ambito.com/dolar/oficial/variacion')
    jsonResponse = V.json()

    print(f"\n *** Variacion USD las {jsonResponse['fecha']} ***")
    print(f"         COMPRA {jsonResponse['compra']} - VENTA {jsonResponse['venta']}\n")

    I = requests.get('https://mercados.ambito.com/dolar/informal/variacion')
    jsonResponse = I.json()

    print(f"\n *** USD Informal las {jsonResponse['fecha']} ***")
    print(f"         COMPRA {jsonResponse['compra']} - VENTA {jsonResponse['venta']}\n")

    T = requests.get('https://mercados.ambito.com/dolarturista/variacion')
    jsonResponse = T.json()

    print(f"\n *** USD Turista las {jsonResponse['fecha']} ***")
    print(f"         COMPRA {jsonResponse['compra']} - VENTA {jsonResponse['venta']}\n")

def borrarPantalla(): #Definimos la función estableciendo el nombre que queramos
    if os.name == "posix":
       os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
       os.system ("cls")

def menu():
        print("Selecciona una entidad para obtenr la cotizacion")
        print("\t1 - Banco Galicia")
        print("\t2 - Dolar SI")
        print("\t3 - Ambito Financiero")
        print("\t0 - Salir")


while True:
    borrarPantalla()
    menu()
    opcionMenu = input("inserta un numero valor >> ")

    if opcionMenu == "1":
        borrarPantalla()
        print("\nCotizacion de Banco Galicia\n")
        bancoGalicia()
        input("\nPulsa una tecla para continuar\n")
    elif opcionMenu == "2":
        borrarPantalla()
        print("\nCotizacion del sitio DolarSI\n")
        DolarSI()
        input("\nPulsa una tecla para continuar\n")
    elif opcionMenu == "3":
        borrarPantalla()
        print("\nCotizacion del sitio Ambito Financiero\n")
        AmbitoFinanciero()
        input("\nPulsa una tecla para continuar\n")
    elif opcionMenu == "0":
        break
    else:
        print("")
        input("No has pulsado ninguna opción correcta...\nPulsa una tecla para continuar")