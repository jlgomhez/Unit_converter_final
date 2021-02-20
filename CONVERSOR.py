from tkinter import *


def doConv():
    cantidadDeSustancia = float(cantidadSustancia.get())
    subindiceDeElemento1 = float(subindiceElemento1.get())
    subindiceDeElemento2 = float(subindiceElemento2.get())
    subindiceDeElemento3 = float(subindiceElemento3.get())
    elemento1Seleccionado = elementoSeleccionado1.get()
    elemento2Seleccionado = elementoSeleccionado2.get()
    elemento3Seleccionado = elementoSeleccionado3.get()
    unidadEntrada = unidadSeleccionadaE.get()
    unidadResultante = unidadSeleccionadaR.get()

    if cantidadDeSustancia >= 0 and subindiceDeElemento1 >=0 and subindiceDeElemento2 >=0 and subindiceDeElemento3 >=0:
        if unidadEntrada == unidadResultante:
            resultado.set(cantidadDeSustancia)
        else:
            if unidadEntrada == "KG" and unidadResultante == "MOL":
                resultado.set(KGMOL(cantidadDeSustancia))
            elif unidadEntrada == "KG" and unidadResultante == "L":
                resultado.set(KGL(cantidadDeSustancia))
            elif unidadEntrada == "MOL" and unidadResultante == "KG":
                resultado.set(MOLKG(cantidadDeSustancia))
            elif unidadEntrada == "MOL" and unidadResultante == "L":
                resultado.set(MOLL(cantidadDeSustancia))
            elif unidadEntrada == "L" and unidadResultante == "KG":
                resultado.set(LKG(cantidadDeSustancia))
            elif unidadEntrada == "L" and unidadResultante == "MOL":
                resultado.set(LMOL(cantidadDeSustancia))

    else:
        mensajeError = Toplevel()
        mensajeErF = Frame(mensajeError)
        mensajeErF.grid(column=0, row=0, sticky=(N, W, E, S))
        Label(mensajeErF, text="Introduzca una cantidad numérica válida!").grid(column=1, row=1)


def KGMOL(masa):
    print("Kilogramo a mol")
    peso1 = float(definirPeso(elementoSeleccionado1.get()))
    peso2 = float(definirPeso(elementoSeleccionado2.get()))
    peso3 = float(definirPeso(elementoSeleccionado3.get()))
    subindice1 = float(subindiceElemento1.get())
    subindice2 = float(subindiceElemento2.get())
    subindice3 = float(subindiceElemento3.get())
    pesoatomico = float(subindice1*peso1 + subindice2*peso2 + subindice3*peso3)
    return masa/pesoatomico


def KGL(masa):
    print("Kilogramo a l")
    peso1 = float(definirPeso(elementoSeleccionado1.get()))
    peso2 = float(definirPeso(elementoSeleccionado2.get()))
    peso3 = float(definirPeso(elementoSeleccionado3.get()))
    subindice1 = float(subindiceElemento1.get())
    subindice2 = float(subindiceElemento2.get())
    subindice3 = float(subindiceElemento3.get())
    pesoatomico = float(subindice1*peso1 + subindice2*peso2 + subindice3*peso3)
    moles = masa/pesoatomico
    return moles*22.4


def MOLKG(moles):
    print("Mol a kilogramo")
    peso1 = float(definirPeso(elementoSeleccionado1.get()))
    peso2 = float(definirPeso(elementoSeleccionado2.get()))
    peso3 = float(definirPeso(elementoSeleccionado3.get()))
    subindice1 = float(subindiceElemento1.get())
    subindice2 = float(subindiceElemento2.get())
    subindice3 = float(subindiceElemento3.get())
    pesoatomico = float(subindice1*peso1 + subindice2*peso2 + subindice3*peso3)
    return moles*pesoatomico


def MOLL(moles):
    print("Mol a litro")
    return moles*22.4


def LKG(litros):
    print("Litro a kilogramo")
    peso1 = float(definirPeso(elementoSeleccionado1.get()))
    peso2 = float(definirPeso(elementoSeleccionado2.get()))
    peso3 = float(definirPeso(elementoSeleccionado3.get()))
    subindice1 = float(subindiceElemento1.get())
    subindice2 = float(subindiceElemento2.get())
    subindice3 = float(subindiceElemento3.get())
    pesoatomico = float(subindice1*peso1 + subindice2*peso2 + subindice3*peso3)
    moles = litros/22.4
    return moles*pesoatomico


def LMOL(litros):
    print("Litro a mol")
    return litros/22.4


def definirPeso(elemento):
    if elemento == "XX":
        return 0
    elif elemento == "H":
        return 0.001008
    elif elemento == "Li":
        return 0.00694
    elif elemento == "Na":
        return 0.02299
    elif elemento == "K":
        return 0.039098
    elif elemento == "Rb":
        return 0.085468
    elif elemento == "Cs":
        return 0.13291
    elif elemento == "Fr":
        return 0.223
    elif elemento == "Be":
        return 0.0090122
    elif elemento == "Mg":
        return 0.024305
    elif elemento == "Ca":
        return 0.04078
    elif elemento == "Sr":
        return 0.08762
    elif elemento == "Ba":
        return 0.13733
    elif elemento == "Ra":
        return 0.226
    elif elemento == "Sc":
        return 0.044956
    elif elemento == "Y":
        return 0.088906
    elif elemento == "Ti":
        return 0.047867
    elif elemento == "Zr":
        return 0.091224
    elif elemento == "Hf":
        return 0.17849
    elif elemento == "Rf":
        return 0.267
    elif elemento == "V":
        return 0.050942
    elif elemento == "Nb":
        return 0.092906
    elif elemento == "Ta":
        return 0.18095
    elif elemento == "Db":
        return 0.268
    elif elemento == "Cr":
        return 0.051996
    elif elemento == "Mo":
        return 0.09595
    elif elemento == "W":
        return 0.18384
    elif elemento == "Sg":
        return 0.269
    elif elemento == "Mn":
        return 0.054938
    elif elemento == "Tc":
        return 0.098
    elif elemento == "Re":
        return 0.18621
    elif elemento == "Bh":
        return 0.270
    elif elemento == "Fe":
        return 0.055845
    elif elemento == "Ru":
        return 0.10107
    elif elemento == "Os":
        return 0.19023
    elif elemento == "Hs":
        return 0.277
    elif elemento == "Co":
        return 0.58933
    elif elemento == "Rh":
        return 0.10291
    elif elemento == "Ir":
        return 0.19222
    elif elemento == "Mt":
        return 0.278
    elif elemento == "Ni":
        return 0.58693
    elif elemento == "Pd":
        return 0.10642
    elif elemento == "Pt":
        return 0.19508
    elif elemento == "Ds":
        return 0.281
    elif elemento == "Cu":
        return 0.063546
    elif elemento == "Ag":
        return 0.10787
    elif elemento == "Au":
        return 0.19697
    elif elemento == "Rg":
        return 0.282
    elif elemento == "Zn":
        return 0.06538
    elif elemento == "Cd":
        return 0.11241
    elif elemento == "Hg":
        return 0.20059
    elif elemento == "Cn":
        return 0.285
    elif elemento == "B":
        return 0.01081
    elif elemento == "Al":
        return 0.026982
    elif elemento == "Ga":
        return 0.069723
    elif elemento == "In":
        return 0.11482
    elif elemento == "Tl":
        return 0.20438
    elif elemento == "Nh":
        return 0.286
    elif elemento == "C":
        return 0.012011
    elif elemento == "Si":
        return 0.028085
    elif elemento == "Ge":
        return 0.07263
    elif elemento == "Sn":
        return 0.11871
    elif elemento == "Pb":
        return 0.2072
    elif elemento == "Fl":
        return 0.289
    elif elemento == "N":
        return 0.14007
    elif elemento == "P":
        return 0.030974
    elif elemento == "As":
        return 0.074922
    elif elemento == "Sb":
        return 0.12176
    elif elemento == "Bi":
        return 0.20898
    elif elemento == "Mc":
        return 0.290
    elif elemento == "O":
        return 0.015999
    elif elemento == "S":
        return 0.03206
    elif elemento == "Se":
        return 0.078971
    elif elemento == "Te":
        return 0.1276
    elif elemento == "Po":
        return 0.209
    elif elemento == "Lv":
        return 0.293
    elif elemento == "Fl":
        return 0.018998
    elif elemento == "Cl":
        return 0.03545
    elif elemento == "Br":
        return 0.079904
    elif elemento == "I":
        return 0.1269
    elif elemento == "At":
        return 0.210
    elif elemento == "Ts":
        return 0.294
    elif elemento == "He":
        return 0.0040026
    elif elemento == "Ne":
        return 0.02018
    elif elemento == "Ar":
        return 0.039948
    elif elemento == "Kr":
        return 0.083798
    elif elemento == "Xe":
        return 0.13129
    elif elemento == "Rn":
        return 0.222
    elif elemento == "Og":
        return 0.294
    elif elemento == "La":
        return 0.13891
    elif elemento == "Ce":
        return 0.14012
    elif elemento == "Pr":
        return 0.14091
    elif elemento == "Nd":
        return 0.14424
    elif elemento == "Pm":
        return 0.145
    elif elemento == "Sm":
        return 0.15036
    elif elemento == "Eu":
        return 0.15196
    elif elemento == "Gd":
        return 0.15725
    elif elemento == "Tb":
        return 0.15725
    elif elemento == "Dy":
        return 0.1625
    elif elemento == "Ho":
        return 0.16726
    elif elemento == "Tm":
        return 0.16893
    elif elemento == "Yb":
        return 0.17305
    elif elemento == "Lu":
        return 0.17497
    elif elemento == "Ac":
        return 0.227
    elif elemento == "Th":
        return 0.23204
    elif elemento == "Pa":
        return 0.23204
    elif elemento == "U":
        return 0.23803
    elif elemento == "Np":
        return 0.237
    elif elemento == "Pu":
        return 0.244
    elif elemento == "Am":
        return 0.243
    elif elemento == "Cm":
        return 0.247
    elif elemento == "Bk":
        return 0.247
    elif elemento == "Cf":
        return 0.251
    elif elemento == "Es":
        return 0.252
    elif elemento == "Fm":
        return 0.257
    elif elemento == "Md":
        return 0.258
    elif elemento == "No":
        return 0.259
    elif elemento == "Lr":
        return 0.266
    else:
        return 0


root = Tk()
root.title("Conversor de unidades")

resultado = IntVar()
resultado.set(0)

listaUnidades = ["KG", "MOL", "L"]
listaElementos = ["XX", "H", "Li", "Na", "K", "Rb", "Cs", "Fr", "Be", "Mg", "Ca", "Sr", "Ba", "Ra", "Sc", "Y", "Ti", "Zr", "Hf", "Rf", "V", "Nb", "Ta", "Db", "Cr", "Mo", "W", "Sg", "Mn", "Tc", "Re", "Bh", "Fe", "Ru", "Os", "Hs", "Co", "Rh", "Ir", "Mt", "Ni", "Pd", "Pt", "Ds", "Cu", "Ag", "Au", "Rg", "Zn", "Cd", "Hg", "Cn", "B", "Al", "Ga", "In", "Tl", "Nh", "C", "Si", "Ge", "Sn", "Pb", "Fl", "N", "P", "As", "Sb", "Bi", "Mc", "O", "S", "Se", "Te", "Po", "Lv", "F", "Cl", "Br", "I", "At" , "Ts", "F", "Cl", "Br", "I", "At", "Ts", "He", "Ne", "Ar", "Kr", "Xe", "Rn", "Og", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr"]

cantidadSustancia = Label(root, text="Cantidad de sustancia:")
cantidadSustancia.grid(row=0, column=0, sticky=E)

cantidadSustancia = Entry(root, width=10)
cantidadSustancia.insert(END, '0')
cantidadSustancia.grid(row=0, column=1)

unidadSeleccionadaE = StringVar()
unidadSeleccionadaE.set(listaUnidades[0])
menuUnidadesE = OptionMenu(root, unidadSeleccionadaE, *listaUnidades)
menuUnidadesE.grid(row=0, column=2)

elementoSeleccionado1 = StringVar()
elementoSeleccionado1.set(listaElementos[0])
menuElemento1 = OptionMenu(root, elementoSeleccionado1, *listaElementos)
menuElemento1.grid(row=0, column=3)

subindiceElemento1 = Entry(root, width=5)
subindiceElemento1.insert(END, '0')
subindiceElemento1.grid(row=0, column=4)

elementoSeleccionado2 = StringVar()
elementoSeleccionado2.set(listaElementos[0])
menuElemento2 = OptionMenu(root, elementoSeleccionado2, *listaElementos)
menuElemento2.grid(row=0, column=5)

subindiceElemento2 = Entry(root, width=5)
subindiceElemento2.insert(END, '0')
subindiceElemento2.grid(row=0, column=6)

elementoSeleccionado3 = StringVar()
elementoSeleccionado3.set(listaElementos[0])
menuElemento3 = OptionMenu(root, elementoSeleccionado3, *listaElementos)
menuElemento3.grid(row=0, column=7)

subindiceElemento3 = Entry(root, width=5)
subindiceElemento3.insert(END, '0')
subindiceElemento3.grid(row=0,column=8)

cantidadResultante = Label(root, text="Resultado :")
cantidadResultante.grid(row=0, column=9, sticky=E)

cantidadResultanteN = Label(root, textvariable=resultado)
cantidadResultanteN.grid(row=0, column=10, sticky=W)

unidadSeleccionadaR = StringVar()
unidadSeleccionadaR.set(listaUnidades[0])
menuUnidadesR = OptionMenu(root, unidadSeleccionadaR, *listaUnidades)
menuUnidadesR.grid(row=0, column=11)

botonConvertir = Button(root, text="Convertir", command=doConv)
botonConvertir.grid(row=1, column=5)

root.mainloop()