'''
funciones auxiliares del juego Ahorcado
'''
 
def carga_archivo_texto(archivo:str)-> list:
    '''
    Carga un archivo de texto y devuelveuna lista con las oraciones del archivo
    '''
 
    with open(archivo,'r') as file:
        oraciones = file.readlines()
    return oraciones  
 
def carga_plantillas(nombre_plantilla)->dict:
    '''
    Carga las plantillas del juego a partir de un archivo de un texto
    '''  
    plantillas = {}
    for i in range(5):
        plantillas[i] = carga_archivo_texto(f'./plantillas/{nombre_plantilla}-{i}.txt')
    return plantillas
 
def despliega_plantilla(diccionario:dict, nivel:int):
    '''
    Despliega una pklanitilla del juego
    '''
    plantilla = diccionario[nivel]
    for renglon in plantilla:
        print(renglon)
 
if __name__ == '__main__':
    plantilla = carga_plantillas('plantilla')
    despliega_plantilla(plantilla,0)
    despliega_plantilla(plantilla,1)