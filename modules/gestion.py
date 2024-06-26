from modulos.data import ruta_j , ruta_h, menup
from modulos.construccion import constr_menup, sol_ans, ver, sol_busqueda, buscar,  añadir, sol_eliminar , eliminar, exportar
'''
gestion del inventario de pinturas
'''
while True:
    constr_menup(menup)
    ans = sol_ans()
    if ans == '1':
        ver(ruta_j)
    elif ans == '2':
        añadir(ruta_j)
    elif ans == '3':
        buscar(sol_busqueda(),ruta_j)
    elif ans == '4':
        eliminar(sol_eliminar(),ruta_j)
    elif ans == '5':
        pass
    else:
        print('coloque una opcion valida\n')


