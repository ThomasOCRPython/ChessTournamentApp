from datetime import datetime
from models.match import Match
class Round:
    def __init__(self, round_name):
        self.round_name=round_name
        self.date_time_start=''
        self.date_time_end=''
        self.matchs=[]
        self.list_of_match=[]
        
    def add_match(self,match):
        self.matchs.append(match)    
     
    # def add_match(self, player1, player2): #1
    #     match = Match(player1, player2)
    #     self.matchs.append(match)
    def datetime_end(self):
        self.date_time_end=datetime.now()
    def __str__(self):
        return f" round_name : {self.round_name} \n date_time_start : {self.date_time_start} \n date_time_end : {self.date_time_end} \n matchs : {self.matchs}"   