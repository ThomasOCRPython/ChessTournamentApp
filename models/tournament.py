
from tinydb import TinyDB, Query,where



class Tournament:
    def __init__(self, name, place, date, time_control, nb_of_rounds=4):
        self.name=name
        self.place=place
        self.date=date
        self.nb_of_rounds=nb_of_rounds
        self.rounds=[]#rounds
        self.players=[]#players
        self.time_control=time_control
        # self.description=description
        # self.round_instance_list=round_instance_list
          
    def add_round(self,round):
        self.rounds.append(round)

    def add_player(self,player):
        self.players.append(player)       

    def __str__(self):
        return f" name : {self.name} \n place : {self.place} \n date : {self.date} \n nb_of_rounds : {self.nb_of_rounds} \n players : {self.players} \n time_control : {self.time_control}"
    
    def serializer(self):
        data = {"name" : self.name,
                "place" : self.place,
                "date" :self.date,
                "nb_of_rounds" : self.nb_of_rounds,
                "rounds" : [round.serializer() for round in self.rounds],
                "players" : [player.serializer() for player in self.players],
                
                }
        return data
        
    def save(self):
        db=TinyDB('db.json',indent=4)
        tournament=db.table('tournament')
        tournament.insert(self.serializer())
             

    def remove(self,id):
        db=TinyDB('db.json',indent=4)
        tournament=db.table('tournament')
        tournament.remove(doc_ids=[id])

    def table_tournament_not_finished(self):
        db=TinyDB('db.json', indent=4)
        tournament=db.table('tournament')
        all_tournament=tournament.all()
        for tournament in all_tournament:
            if len(tournament['rounds'])!=4:
                print(tournament.doc_id, tournament['name'])

    def load_id_table(self,tournament):
        db=TinyDB('db.json', indent=4)
        tournament=db.table('tournament')
        tournament_id = tournament.doc_id
        return tournament_id

    def load_tournament_table(self,id_tournament):
        db=TinyDB('db.json', indent=4)
        tournament=db.table('tournament')
        tournament = tournament.get(doc_id=id_tournament)
        return tournament
        #print (tournament)

    