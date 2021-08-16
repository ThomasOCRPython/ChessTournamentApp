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
        # round_date_time_start=
        # round_date_time_end=
        self.round=Round(round_name)
        tournament_controller.add_round(self.round)
        print(round_name)#,round_date_time_start,round_date_time_end)
       
       

    @staticmethod
    def __get_date_time_start(message):
        get_date= view.get_input(message)
        while True:
            try:
                datetime.strptime(get_date, "%d/%m/%Y,%H:%M:%S")
                break
            except ValueError :
                get_date=view.get_input(f"Error: {message}")

        return get_date
    @staticmethod
    def __get_date_time_end(message):
        get_date= view.get_input(message)
        while True:
            try:
                datetime.strptime(get_date, '%d/%m/%Y,%H:%M:%S')
                break
            except ValueError :
                get_date=view.get_input(f"Error: {message}")

        return get_date