from controllers.constantPlayer import NUM_OF_PLAYER
from views import tournament_view as view
from models.round import Round
from datetime import datetime
class RoundController:
    
    def create_round(self,round_name):
        self.round_name=round_name
        for i in NUM_OF_PLAYER/2:
         round_date_time_start=self.__get_date_time_start("Enter date time start")
         round_date_time_end=self.__get_date_time_end("Enter date time end")
        round=Round(round_name,round_date_time_start,round_date_time_end)

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