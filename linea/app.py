def main(m: float,b : float):
    '''Funcion principal que calcula las coordenadas de una linea recta 
    Recibimos m y b
    Regresa: nada'''
    m= 2.0
    b = 3.0
    print(coordenadas_enteros)
    XF = [x/10.0 for in range(10,110,5)]
    YF = [funciones.calcular_y(x, m, b) for x in XF]
    coordenadas_flotantes = list(zip(XF,YF))
    print("Flotantes:")
    print(coordenadas_flotantes)

    if__name_ == '__main__':
        parser = argparse.ArgumentParsee()
        parser