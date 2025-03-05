'''Archivo con las funciones necesarias de la aplicacion libro web'''
import csv

def lee_archivo_csv(archivo:str)->list:
#Lee un archivo csv y lo convierte en una lista de diciionarios
    with open(archivo,"r",encoding='utf8')as f:
        return[x for x in csv.DictReader(f)]

def crea_diccionario_titulos(lista:list)->dict:
    '''Crea un diccionario con los titulos como clave y el resto de los datos como valores'''
    return{x['Titulo']: x for x in lista}

if __name__ == '__main__':
    archivo_csv = 'booklist2000.csv'
    lista_libros = lee_archivo_csv(archivo_csv)
    diccionario_libros = crea_diccionario_titulos
    (lista_libros)