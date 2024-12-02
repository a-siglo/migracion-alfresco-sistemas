import os
import shutil
import re

carpeta_origen = '/home/mmunos/Escritorio/cortes/year2017/Proveedores'

# Criterios de busqueda como sufijo del mes
criterios_busqueda = {
    #'01': ['enero', '01_', '01'],  
    '02': ['febrero', '02_', '02','2'],  
    '03': ['marzo', '03_', '03','3'],
    '04': ['abril', '04_', '04','4'],
    '05': ['mayo', '05_', '05','5'],
    '06': ['junio', '06_', '06', '6'],
    '07': ['julio', '07_', '07', '7'],
    '08': ['agosto', '08_', '08','8'],
    '09': ['septiembre', '09_', '09','9'],
    '10': ['octubre', '10_', '10'],
    '11': ['noviembre', '11_', '11'],
    '12': ['diciembre', '12_', '12']
}

meses = { 
    '02': 'Febrero',
    '03': 'Marzo',
    '04': 'Abril',
    '05': 'Mayo',
    '06': 'Junio',
    '07': 'Julio',
    '08': 'Agosto',
    '09': 'Septiembre',
    '10': 'Octubre',
    '11': 'Noviembre',
    '12': 'Diciembre'
}

ruta_base_destino = '/home/mmunos/Escritorio/Migracion-Alfresco-Sistemas/recursos/Cortes/Agrupacion carpetas por mes/2017/Proveedores'

def encontrar_mes(archivo):
    for numero_mes, sufijos in criterios_busqueda.items():
        for sufijo in sufijos:
            #if re.search(rf'{sufijo.lower()}', archivo.lower()):
            if sufijo.lower() in archivo.lower():
                return numero_mes
    return None

for archivo in os.listdir(carpeta_origen):
    ruta_completa_origen = os.path.join(carpeta_origen, archivo)
    numero_mes = encontrar_mes(archivo)
    
    if numero_mes:
        carpeta_destino = os.path.join(ruta_base_destino, f'{numero_mes}.{meses[numero_mes]}')
        if not os.path.exists(carpeta_destino):
            os.makedirs(carpeta_destino)
        
        ruta_completa_destino = os.path.join(carpeta_destino, archivo)
        shutil.move(ruta_completa_origen, ruta_completa_destino)
        print(f"Se movió el archivo '{archivo}' a la carpeta de {meses[numero_mes]}  Búsqueda:{criterios_busqueda[numero_mes]}")
    else:
        print(f"No se pudo clasificar el archivo '{archivo}'")

