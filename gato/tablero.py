'''
tablero.py: Dibuja el tablero del juego de el gato
'''
import random
 
def dibuja_tablero(simbolos:dict):
    print(f'''
           {simbolos['1']} | {simbolos['2']} | {simbolos['3']}
          ----------
           {simbolos['4']} | {simbolos['5']} | {simbolos['6']}
          ----------
           {simbolos['7']} | {simbolos['8']} | {simbolos['9']}
          ----------
         ''' )
 
def ia(simbolos:dict):
    '''Juega la maquina'''
    ocupado = True
    while ocupado == True:
        x = random.choice(list(simbolos.keys()))
        if simbolos[x] not in ['X','O']:
            simbolos[x] = 'O'
            ocupado = False
 
 
def usuario(simbolos:dict):
    '''Juega el usuario'''
    numeros = [str(i) for i in range(1,10)]
    ocupado = True
    while ocupado == True:
        x = input('Ingresa el numero de la casilla: ')
        if (x in numeros):
          if simbolos[x] not in ['X','O']:
            simbolos[x] = 'X'
            ocupado = False
          else:
            print('Casilla ocupada')    
        else: print('Valor invalido, ingresa un  numero del 1 al 9')    
 
def juego(simbolos:dict):
  '''juego de gato'''
  lista_combinaciones = [
    ['1','2','3'],
    ['4','5','6'],
    ['7','8','9'],
    ['1','4','7'],
    ['2','5','8'],
    ['3','6','9'],
    ['1','5','9'],
    ['3','5','7']
  ]
  en_juego = True
  gana = None
  movimientos = 0
  dibuja_tablero(simbolos)
  while en_juego:
      usuario(simbolos)
      dibuja_tablero(simbolos)
      movimientos += 1
      gana = checa_winner(simbolos,lista_combinaciones)
      if gana is not None:
        en_juego = False
        continue
      if movimientos >= 9:
        en_juego = False
        continue
      ia(simbolos)
      dibuja_tablero(simbolos)
      movimientos += 1
      gana = checa_winner(simbolos,lista_combinaciones)
      if gana is not None:
        en_juego = False
        continue
      if movimientos >=9:
        en_juego = False
        continue
  return gana
   
def checa_winner(simbolos:dict, combinaciones:list):
  '''Checa si hay un ganador'''
  for c in combinaciones:
    if simbolos[c[0]] == simbolos[c[1]] == simbolos[c[2]]:
      return simbolos[c[0]]
    return None  
 
