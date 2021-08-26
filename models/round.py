# from datetime import datetime
import datetime
from models.match import Match
class Round:
    def __init__(self, round_name):
        self.round_name=round_name
        self.date_time_start=''
        self.date_time_end=''
        self.matchs=[]
        self.matchs_serializ=[]

    def add_match(self,match):
        self.matchs.append(match) 

    def add_match_serializ(self,match_serializ):
        self.matchs_serializ.append(match_serializ)

    def datetime_end(self):
        self.date_time_end=datetime.datetime.now()

    def __str__(self):
        return f" round_name : {self.round_name} \n date_time_start : {self.date_time_start} \n date_time_end : {self.date_time_end} \n matchs : {self.matchs}"   
    
    def serializer(self):
        data = {"round_name" : self.round_name,
                "date_time_start" : self.date_time_start,
                "date_time_end" : self.date_time_end,
                #"matchs" : [match.match_serializer() for match in self.matchs]
                "matchs_serializ":[ match for match in self.matchs_serializ]}
        return data