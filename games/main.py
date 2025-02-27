''' Programa principal de games '''
from Athlete import Athlete
from Sport import Sport
from Game import Game
from Team import Team
import json
 
def main(archivo_torneo:str):
    ''' Funcion principal de game '''
    if archivo_torneo != "":
        with open(archivo_torneo, "r") as file:
            torneo = json.load(archivo_torneo)
    else:
        players_mexico = ['Chicarito','Chucky','Ochoa','Tecatito','Guardado','Herrera','Layun','Moreno','Araujo','Oribe','Gimenez']
        players_espania = ['Casillas','Ramos','Pique','Iniesta','Silva','Isco','Busquets','Costa','Morata','Asensio','Pedri']
        players_brasil = ['Neymar', 'Coutinho', ' Mercelo', 'Casemiro', 'Alisson', 'Jesus', ' Paulinho', 'Thiago', 'Silva', 'Fermino', 'Danilo']
        players_argentina = ['Messi', 'Aguero', 'DiMaria', ' Mascherano', 'Higuain', 'Dybala', 'Otamendi', 'Romero', 'Riquelme', 'Dibu', 'Kempes']
        lista_mexico = [Athlete(x) for x in players_mexico]
        lista_espania = [Athlete(x) for x in players_espania]
        lista_brasil = [Athlete(x) for x in players_brasil]
        lista_argentina = [Athlete(x) for x in players_argentina]
        soccer = Sport("Soccer", 11, "FIFA")
        mexico = Team("Mexico", soccer, lista_mexico)
        espania = Team("Espania", soccer, lista_espania)
        brasil = Team("Brasil", soccer, lista_brasil)
        argentina = Team("Argentina", soccer, lista_argentina)
        equipos = [mexico, espania, brasil, argentina]
        d = {}
        for local in equipos:
            for visitante in equipos:
                if local != visitante:
                    juego = Game(local, visitante)
                    partido = f'{local} - {visitante}'
                    partido_2 = f'{visitante} - {local}'
                    if partido_2  not in d:
                        d[partido] = juego.to_json()
       
        torneo = list(d.values())
        archivo_torneo = "torneo.json"
        with open(archivo_torneo, "w", encoding='utf8') as f:
            json.dump(torneo, f, ensure_ascii=False, indent=4)
 
        print(f"Se escribio archivo '{archivo_torneo}'satisfactoriamente")
 
    # Jugar todos los juegos del torneo
    for juego in torneo:
        A = Team(juego['A']['name'], Sport(juego['A']['sport']['name'], juego['A']['sport']['players'], juego['A']['sport']['league']), [Athlete(x['name']) for x in juego['A']['players']])
        B = Team(juego['B']['name'], Sport(juego['B']['sport']['name'], juego['B']['sport']['players'], juego['B']['sport']['league']), [Athlete(x['name']) for x in juego['B']['players']])
        game = Game(A, B)
        game.play()
        print(game)
        print("----------------")
 
if __name__ == "__main__":
    archivo_torneo = ""
    main(archivo_torneo)