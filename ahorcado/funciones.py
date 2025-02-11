'''
funciones auxiliares del juego del ahorcado
'''

def carga_archivo_texto(archivo:str)->list:
    '''
    carga un archivo de texto y devuelve una lista on las orcaiones del archivo
    '''
    with open(archivo, 'r') as file:
        oraciones = file.readlines()
    return oraciones

if __name__ == '__main__':
    lista = carga_archivo_texto("c:/ESCUELA/desarrollo 4/curso_python-1/ahorcado/plantilla/plantilla-0.txt")
    for elemento in lista:
        print(elemento)