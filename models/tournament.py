
class Tournament:
    def __init__(self, name, place, date, time_control,description, round_instance_list, nb_of_rounds=4):
        self.name=name
        self.place=place
        self.date=date
        self.nb_of_rounds=nb_of_rounds
        self.rounds=[]#rounds
        self.players=[]#players
        self.time_control=time_control
        self.description=description
        self.round_instance_list=round_instance_list
          
    
    def add_round(self,round):
        self.round.append(round)
    def add_player(self,player):
        self.players.append(player)    

        

    def __str__(self):
        pass


    