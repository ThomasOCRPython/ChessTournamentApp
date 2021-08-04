from controllers.matchController import MatchController
from models.match import Match
from controllers.constantPlayer import NUM_OF_PLAYER
from views import tournament_view as view
from models.round import Round
from datetime import datetime
class RoundController:
    
    def create_round(self,name,tournament_controller):
       
        round_name="Round"+str(name)
        round_date_time_start="12/12/2021,12:12:00"#self.__get_date_time_start("Enter date time start")
        round_date_time_end="12/12/2021,13:12:00"#self.__get_date_time_end("Enter date time end")
        round=Round(round_name,round_date_time_start,round_date_time_end)
        #round.add_match(match)
        tournament_controller.add_round(round)
        print(round_name,round_date_time_start,round_date_time_end)
        #match=MatchController(self.round.matchs)
       

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