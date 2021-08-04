
from controllers.roundController import RoundController
from datetime import datetime
from controllers import matchController, player_controller
from models import tournament
from models import player
from models.round import Round 
from models.tournament import Tournament
from models.player import Player
from views import tournament_view as view
from controllers.player_controller import PlayerController
from controllers.constantPlayer import NUM_OF_PLAYER

#NUM_OF_PLAYER=8
class TournamentController:
    
    

    def __init__(self):
        self.tournament=None
    

    def create_new_tournament(self):
        tournament_name="Pegasus"#self.__get_name("Enter tournament name: ")
        tournament_place="kotte"#self.__get_place("Enter tournament place: ")
        tournament_date="30/07/2021"#self.__get_date("Enter the date of the tournament : ")
        tournament_get_time_control="1"#self.__get_time_control("Enter '1' for 'bullet', '2' for 'blits', '3' for 'coup rapide' :")
        # tournament_description=self.__get_description("Enter description")
        self.tournament=Tournament(tournament_name,tournament_place,tournament_date,tournament_get_time_control)
        self.player_controller=PlayerController()
        self.player_controller.create_player(self.tournament)
        list_of_match=self.__list_of_match()
        self.__create_round_one(self.tournament,list_of_match)
        
        
        #self.__list_of_match()
        
        #self.__first_round()
       
    # def __first_round(self):   
    #     Round.round_name = Round("1")
    # #for ...
    #     #round.add_match(match)
    # #self.tournament.add_round(round)
    
    @staticmethod
    def __get_name(message):
        name=view.get_input(message)
        while not name.isalpha():
            name=view.get_input(f"Error: {message}")
        return name 
    @staticmethod
    def __get_place(message):
        place=view.get_input(message)
        while not place.isalpha():
            place=view.get_input(f"Error: {message}")
        return place 
    @staticmethod
    def __get_date(message):
        get_date= view.get_input(message)
        while True:
            try:
                datetime.strptime(get_date, '%d/%m/%Y')
                break
            except ValueError :
                get_date=view.get_input(f"Error: {message}")

        return get_date
    @staticmethod
    def __get_time_control(message):
        time_control=view.get_input(message)
        while time_control not in ("1", "2", "3"):
            time_control=view.get_input(f"Error: {message}")
        if time_control==1:
            time_control="bullet"
        elif time_control==2:
            time_control="blitz"
        else:time_control= "coup rapide"
        return time_control
    @staticmethod
    def __get_description(message):
        description=view.get_input(message)
        return description

    def __create_round_one(self,tournament,list_of_match):
        round=RoundController()
        round.create_round("1",tournament)
        for match in list_of_match:
            match=matchController()
            match.create_match(list_of_match,round)



       
    def __list_of_match(self):
        self.tournament.players.sort(key = lambda x: x.elo)
        affichage=self.tournament.players
        print (len(affichage))
        for i in range(int(len(affichage) / 2)):
            return affichage[i], affichage[i+int(len(affichage) / 2)]
        
        

    # def __run_other_round(self, name):
    #     round = Round(name)
    #     pass
    
    def __str__(self):
            return f" name : {self.tournament.players[player]} "
            
