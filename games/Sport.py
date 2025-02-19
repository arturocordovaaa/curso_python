class Sport:
    '''Clase para representar un deporte
    '''
    def __init__(self, name:str, players:int, league:str):

        self.name = name
        if isinstance(players, int):
            self.players = players
        else:
            self.players = int(players)
        self.league = league 
    
    def __str__(self):
        '''Representacion en string de sport'''
        return f"Sport: {self.name}, {self.players}, {self.league}"
    
    def __repr__(self)->str:
        '''Representacion en strig de sport'''
        return f"Sport(name = '{self.name}', players={self.players}, league='{self.league}')"
    
    def to_json(self)->dict:
        '''Converti sport a json'''
        return{"name":self.name,"players":self.players, "league":self.league}
    
if __name__ =="__main__":
    nfl = Sport("Football", 11,"NFL")
    print(nfl)
    print(repr(nfl))
    print(nfl.to_json())
    lmp = Sport("Baseball", "9","LMP")
    print(lmp)
    print(repr(lmp))
    print(lmp.to_json())