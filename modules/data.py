from pathlib import Path

home  = Path(__file__).parent.parent

ruta_j = Path(home/'base.json')
ruta_h = Path(home/'exportar.csv')

menup =['ver listado de pintura',
         'buscar pintura', 
         'agregar pintura', 
         'eliminar pintura', 
         ' exportar pintura']
