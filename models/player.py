from tinydb import TinyDB, Query
from operator import itemgetter
class Player:
    def __init__(self, last_name, name, date_of_bird, sex, elo, score=0):
        self.last_name=last_name
        self.name=name
        self.date_of_bird=date_of_bird
        self.sex=sex
        self.elo=elo
        self.score=score
        #self.id=id
        self.oponents=[]
    
    def add_oponent(self,oponent):
        self.oponents.append(oponent)

    def __str__(self):
        return f"last_name : {self.last_name} \n name : {self.name} \n date_of_bird : {self.date_of_bird} \n sex : {self.sex} \n elo : {self.elo} \n score : {self.score} \n oponent : {self.oponents}"

    def serializer(self):
        data = {"last_name" : self.last_name,
                "name" : self.name,
                "date_of_bird" : self.date_of_bird,
                "sex" : self.sex,
                "elo" : self.elo,
                "score": self.score,
                "oponents" : self.oponents}
                #"oponents":[oponent for oponent in self.oponents]}
        return data
    
    def save(self):
        db=TinyDB('db.json',indent=4)
        player=db.table('player') 
        player.insert(self.serializer())

    def table_players(self):
        order_player=[]
        db=TinyDB('db.json', indent=4)
        player=db.table('player')
        all_players=player.all()
        for player in all_players:
            order_player.append((player.doc_id,player["name"],player["elo"]))
        # for player in all_players:
        #     print("=============== PLAYER :",player.doc_id, player['name']," ELO :",player["elo"],"===============")
        sorted_apha=sorted(order_player, key=lambda player: player[2])
        print (sorted(sorted_apha, key=lambda player: player[1]))
        
        