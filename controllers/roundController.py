
from controllers.matchController import MatchController
from models.match import Match
from controllers.constantPlayer import NUM_OF_PLAYER
from views import tournament_view as view
from models.round import Round
from datetime import datetime
class RoundController:
    def __init__(self) :
        pass
    def create_round(self,name,tournament_controller):
        round_name="Round"+str(name)
        self.round=Round(round_name)
        self.round.date_time_start=datetime.now()
        tournament_controller.add_round(self.round)
        print(round_name,"     ---","[ROUND :",f"{name}]","---")#,round_date_time_start,round_date_time_end)
        print("date start :",self.round.date_time_start)
        
    
           
    
       