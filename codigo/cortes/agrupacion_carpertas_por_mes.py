import os
import shutil
import re

carpeta_origen = '/home/mmunos/Escritorio/cortes/year2017/Proveedores'

# Criterios de busqueda como sufijo del mes
criterios_busqueda = {
    '01': ['enero', '01_', '01','1_'],  
    '02': ['febrero', '02_', '02','2_'],  
    '03': ['marzo', '03_', '03','3_'],
    '04': ['abril', '04_', '04','4_'],
    '05': ['mayo', '05_', '05','5_'],
    '06': ['junio', '06_', '06','6_'],
    '07': ['julio', '07_', '07','7_'],
    '08': ['agosto', '08_', '08','8_'],
    '09': ['septiembre', '09_', '09','9_'],
    '10': ['octubre', '10_', '10'],
    '11': ['noviembre', '11_', '11'],
    '12': ['diciembre', '12_', '12']
}

meses = {
    '01': 'Enero',
    '02': 'Febrero',
    '03': 'Marzo',
    '04': 'Abril',
    '05': 'Mayo',
    '06': 'Junio',
    '07': 'Julio',
    '08_': 'Agosto',
    '09': 'Septiembre',
    '10': 'Octubre',
    '11': 'Noviembre',
    '12': 'Diciembre'
}




ruta_base_destino = '/home/mmunos/Escritorio/Migracion-Alfresco-Sistemas/recursos/Cortes/Agrupacion carpetas por mes/2017/Proveedores'

for numero_mes, sufijos in criterios_busqueda.items(): # Cada criterio de búsqueda
    carpeta_destino = os.path.join(ruta_base_destino, f'{numero_mes}.{meses[numero_mes]}') #Crear carpeta destino
    
    if not os.path.exists(carpeta_destino):#Si no existe la carpeta, crearla.
        os.makedirs(carpeta_destino)
    
    for archivo in os.listdir(carpeta_origen): # Recorrer los archivos en la carpeta de origen
        ruta_completa_origen = os.path.join(carpeta_origen, archivo)
        
        for sufijo in sufijos:  # Verificar si el nombre del archivo contiene el número de mes y alguno de los sufijos
            if re.search(rf'{sufijo}', archivo, re.IGNORECASE):
                ruta_completa_destino = os.path.join(carpeta_destino, archivo) # ruta completa de destino
                shutil.move(ruta_completa_origen, ruta_completa_destino) # Mover el archivo al destino
                
                print(f"Se movió el archivo '{archivo}' a la carpeta de {meses[numero_mes]}  Búsqueda:{sufijo}")
                break



