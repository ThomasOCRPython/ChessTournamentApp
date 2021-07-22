from datetime import datetime, time
from models.tournament import Tournament
# from models.player import Player
from views import tournament_view as view
from controllers.player_controller import create_player

NUM_OF_PLAYER=8
class TournamentController:
    

    def __init__(self):
        self.tournament=None

    def create_new_tournament(self):
        tournament_name=self.__get_name("Enter tournament name: ")
        tournament_place=self.__get_place("Enter tournament place: ")
        tournament_date=self.__get_date("Enter the date of the tournament : ")
        tournament_get_time_control=self.__get_time_control("Enter '1' for 'bullet', '2' for 'blits', '3' for 'coup rapide' :")
        tournament_description=self.__get_description("Enter description")
        self.tournament=Tournament(tournament_name,tournament_place,tournament_date,tournament_get_time_control,tournament_description)
        create_player()
       
    def __first_round(self):
        pass
    #round = Round("1")
    #for ...
        #round.add_match(match)
    #self.tournament.add_round(round)

    @staticmethod
    def __get_name(message):
        name=view.get_name(message)
        while not name.isalpha():
            name=view.get_name(f"Error: {message}")
        return name 
    @staticmethod
    def __get_place(message):
        place=view.get_place(message)
        while not place.isalpha():
            place=view.get_place(f"Error: {message}")
        return place 
    @staticmethod
    def __get_date(message):
        get_date= view.get_date(message)
        while True:
            if datetime.strptime(get_date, '%m/%d/%Y %I:%M %p')==False:
                get_date=view.get_date(f"Error: {message}")
            else:
                break
        return get_date
    @staticmethod
    def __get_time_control(message):
        time_control=view.get_time_control(message)
        while time_control not in ("1", "2", "3"):
            place=view.get_time_control(f"Error: {message}")
        if time_control==1:
            time_control="bullet"
        elif time_control==2:
            time_control="blitz"
        else:time_control= "coup rapide"
        return time_control
    @staticmethod
    def __get_description(message):
        description=view.get_description(message)
        return description

if __name__=="__main__":
    tournamentController=TournamentController()
    tournamentController.create_new_tournament()
