
import json


def constr_menup(lista):
    for ind, opt in enumerate(lista):
        print(f'{ind + 1} . {opt}')

def sol_ans():
    sss = input('¿Que quieres hacer?\n')
    return sss

def ver(ruta_h):
    if not ruta_h.exists():
        ruta_h.touch
    if ruta_h.stat().st_size==0:
        print('el archivo esta vacio')
        json_f = []
        cod = 380560
    else:
        with open(ruta_h, mode='r') as stream:
            json = json.load(stream)
            cod = []
        for elem in json_f:
            print(elem)

def sol_buscar():
    rep = input('ingrese el codigo o nombre de la pintura que quiere buscar')
    return rep

def buscar(dato, ruta_h):
    if not ruta_h.exists():
        ruta_h.touch
    if ruta_h.stat().st_size==0:
        print('el archivo esta vacio')
        json_f = []
        cod = 380560
    else:
        with open(ruta_h, mode='r') as stream:
            json = json.load(stream)
            cod = []
            for elem in json_f:
                if str(elem({"CODIGO"})) == dato or dato in elem({"NOMBRE"}):
                    print(f'CODIGO: {elem["CODIGO"]}')
                    print(f'NOMBRE: {elem["NOMBRE"]}')
                    print(f'TIPO: {elem["TIPO"]}')
                    print(f'VALOR: {elem["VALOR"]}')
                    print(f'STOCK: {elem["STOCK"]}')

def añadir(ruta_h):
    if not ruta_h.exists():
        ruta_h.touch
    if ruta_h.stat().st_size==0:
        print('el archivo esta vacio')
        json_f = []
        cod = 380560
    else:
        with open(ruta_h, mode='r') as stream:
            json = json.load(stream)
            cod = []
        for elem in json_f:
            cod.append(elem["CODIGO"])
        cod = max(cod) + 1
    while True:
        nom = input('ingrese el nombre de la nueva pintura\n')
        break
    while True:
        tipo = input('ingrese el tipo de pintura\n')
        break
    while True:
        valor = input('ingrese el valor de la pintura\n')
        valor = int(valor)
        break
    while True:
        stock = input('ingrese el stock de la pintura\n')
        stock = int(stock)
        break
    data = {"CODIGO": cod,
            "NOMBRE": nom,
            "TIPO": tipo,
            "VALOR": valor,
            "STOCK": stock}
    json_f.append(data)
    with open(ruta_h, mode='r') as stream:
        json = json.load(stream)
        print('se ha añadido correctamente')

def sol_eliminar():
 rspa =input('ingresa el codigo de la pintura que desea eliminar\n')
 return rspa

def eliminar(dato, ruta_h):
    if not ruta_h.exists():
        ruta_h.touch
    if ruta_h.stat().st_size==0:
        print('el archivo esta vacio')
        json_f = []
        cod = 380560
    else:
        with open(ruta_h, mode='r') as stream:
         json = json.load(stream)
         cod = []


