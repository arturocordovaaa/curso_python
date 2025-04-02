'''Programa principal de MovieDB'''
from flask import Flask, request, url_for , render_template, redirect, session
import os
import random
import movie_classes as mc

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Clave secreta para la sesión
sistema = mc.SistemaCine()
archivo = "datos/actores.csv"
archivo_peliculas = "datos/peliculas.csv"   
archivo_relaciones = "datos/relacion.csv"
archivo_usuarios = "datos/users.csv"
sistema.cargar_csv(archivo, mc.Actor)
sistema.cargar_csv(archivo_peliculas, mc.Pelicula)
sistema.cargar_csv(archivo_relaciones, mc.Relacion)
sistema.cargar_csv(archivo_usuarios, mc.User)




@app.route('/actores')
def actores():
    '''Muestra la lista de actores'''
    actores = sistema.actores.values()
    return render_template('actores.html', actores=actores)

@app.route('/actor/<int:id_actor>')
def actor(id_actor):
    '''Muestra la informacion de un actor y sus peliculas'''
    actor = sistema.actores[id_actor]
    peliculas = sistema.obtener_peliculas_por_actor(id_actor)
    personajes = sistema.obtener_personaje_por_actor(id_actor)
    peliculas_personajes = zip(peliculas, personajes)  
    return render_template('actor.html', actor=actor, peliculas=peliculas, peliculas_personajes=peliculas_personajes)

@app.route('/pelicula/<int:id_pelicula>')
def pelicula(id_pelicula):
    '''Muestra la informacion de una pelicula'''
    pelicula = sistema.peliculas[id_pelicula]
    actores = sistema.obtener_actores_por_pelicula(id_pelicula)
    personajes = sistema.obtener_personaje_por_pelicula(id_pelicula)
    actores_personajes = zip(actores, personajes)
    return render_template('pelicula.html', pelicula=pelicula, actores=actores, actores_personajes=actores_personajes)

@app.route('/peliculas')
def peliculas():
    '''Muestra la lista de peliculas'''
    peliculas = sistema.peliculas.values()
    return render_template('peliculas.html', peliculas=peliculas)

@app.route('/')
def index():
    '''Página principal de la aplicación'''
    peliculas = list(sistema.peliculas.values())  
    peliculas_destacadas = random.sample(peliculas, min(len(peliculas), 3))  
    return render_template('index.html', peliculas=peliculas_destacadas)

@app.route('/login', methods=['GET', 'POST'])
def login():
    '''Muestra el formulario de login'''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        exito = sistema.login(username, password)
        if exito:
            session['logged_in'] = True
            session['username'] = sistema.usuario_actual.nombre_completo
            return redirect(url_for('index'))
        else:
            error = 'Usuario o contraseña incorrectos'
            return render_template('login.html', error=error)
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
    