#!/usr/bin/python
import requests
import os
from tkinter import *
from tkinter.ttk import *

def bancoGalicia():

    newWindow = Toplevel(master)
    newWindow.title("Cotizacion Banco Galicia")
    newWindow.geometry("200x100")
    Label(newWindow, text="\nCotizacion Banco Galicia\n").pack()
    r = requests.get('https://www.bancogalicia.com/cotizacion/cotizar?currencyId=02&quoteType=SU&quoteId=999')
    jsonResponse = r.json()

    for key, value in jsonResponse.items():

        if key == 'error':
            Label(newWindow, text="Disculpe pero en este momento no es posible conseguir la cotizacion \nIntente nuevamente mas tarde").pack()
        else:
            if key == 'buy':
                Label(newWindow, text="Dolar Compra es de " + value).pack()
            elif key == 'sell':
                Label(newWindow, text="Dolar Venta es de " + value).pack()

def DolarSI():

    newWindow = Toplevel(master)
    newWindow.title("Dolar Si")
    newWindow.geometry("200x100")
    Label(newWindow, text="\nCotizacion de Dolar Si\n").pack()

    r = requests.get('https://www.dolarsi.com/api/api.php?type=cotizador')
    jsonResponse = r.json()

    for data in jsonResponse:
        nombre = data['casa']['nombre']
        if nombre == "Dolar":
            venta = data['casa']['venta']
            compra = data['casa']['compra']
            Label(newWindow, text="Dolar Venta es de " + venta).pack()
            Label(newWindow, text="Dolar Compra es de " + compra).pack()


def AmbitoFinanciero():

    newWindow = Toplevel(master)
    newWindow.title("Ambito Financiero")
    newWindow.geometry("300x350")
    Label(newWindow, text="\nCotizacion de Ambito\n").pack()

    V = requests.get('https://mercados.ambito.com/dolar/oficial/variacion')
    jsonResponse = V.json()
    Label(newWindow, text="\nVariacion USD a las "+jsonResponse['fecha']+"\n").pack()
    Label(newWindow, text="Dolar Compra es de " + jsonResponse['compra']).pack()
    Label(newWindow, text="Dolar Venta es de " + jsonResponse['venta']).pack()


    I = requests.get('https://mercados.ambito.com/dolar/informal/variacion')
    jsonResponse = I.json()
    Label(newWindow, text="\nInformal USD a las "+jsonResponse['fecha']+"\n").pack()
    Label(newWindow, text="Dolar Compra es de " + jsonResponse['compra']).pack()
    Label(newWindow, text="Dolar Venta es de " + jsonResponse['venta']).pack()

    T = requests.get('https://mercados.ambito.com/dolarturista/variacion')
    jsonResponse = T.json()
    Label(newWindow, text="\nTurista USD a las " + jsonResponse['fecha'] + "\n").pack()
    Label(newWindow, text="Dolar Compra es de " + jsonResponse['compra']).pack()
    Label(newWindow, text="Dolar Venta es de " + jsonResponse['venta']).pack()

master = Tk()
master.geometry("300x200")
master.title("pyDolar")

label = Label(master, text="Seleccione la Entidad")
label.pack(pady=10)
btn = Button(master, text="Banco Galicia", command=bancoGalicia)
btn.pack(pady=10)
btn = Button(master, text="Dolar Si", command=DolarSI)
btn.pack(pady=10)
btn = Button(master, text="Ambito", command=AmbitoFinanciero)
btn.pack(pady=10)

mainloop()
