
from models import tournament
from models.tournament import Tournament
from controllers import constantPlayer as const
from views import tournament_view as view
from models.player import Player
# from datetime import datetime
import datetime




class PlayerController:

    players=[Player("Duval","Thomas","03-09-1978","M",1,0,),Player("Gonage","Ranga","03-09-1998","M",2,0,),Player("Duval","Hélène","01-01-1981","F",3,0,),Player("Xczero","Android","01-09-2978","N",4,0,),Player("Einstein","Albert","14-03-1879","M",5,0,),Player("Einstein","Robert","14-03-1879","M",6,0,),Player("Margaret","Hamilton","03-09-1938","M",7,0,),Player("Davinci","George","03-09-1988","M",8,0,)]
    def create_player(self, tournament_controller):
        
        '''for i in range(const.NUM_OF_PLAYER):
            player_last_name=self.__get_last_name("Enter player last name : ")
            player_name=self.__get_name("Enter player first name : ")
            player_date_of_bird=self.__get_date_of_bird("Enter player date of bird : ")
            player_sex=self.__get_sex("Enter sex player 'M' for male, 'F'for female 'N'for none: ")
            player_elo=self.__get_elo("Enter player Elo : ")
            player_score=self.__get_score("Enter score player : ")
            player =Player(player_last_name,player_name,player_date_of_bird,player_sex, player_elo,player_score)'''
            # tournament_controller.add_player(player)
        for player in self.players:
            tournament_controller.add_player(player)
            Player.save(player)

    @staticmethod
    def __get_name(message):
        name=view.get_input(message)
        while not name.isalpha():
            name=view.get_input(f"Error: {message}")
        return name 
    @staticmethod
    def __get_elo(message):
        elo= view.get_input(message)
        while not elo.isnumeric():
            elo=view.get_input(f"Error: {message}")
        return int(elo) 
    @staticmethod
    def __get_last_name(message):
        last_name= view.get_input(message)
        while not last_name.isalpha():
            last_name=view.get_input(f"Error: {message}")
        return last_name    
    @staticmethod
    def __get_date_of_bird(message):
        get_date_of_bird= view.get_input(message)
        while True:
            try:

                datetime.datetime.strptime(get_date_of_bird, '%d/%m/%Y')
                break
            except ValueError:
                get_date_of_bird=view.get_input(f"Error: {message}")
        return get_date_of_bird       
    @staticmethod
    def __get_sex(message):
        sex= view.get_input(message)
        while sex not in ("M", "F", "N"):
            sex=view.get_input(f"Error: {message}")
        return sex 
    @staticmethod
    def __get_score(message):
        score= view.get_input(message)
        while not score.isnumeric():
            score=view.get_input(f"Error: {message}")
        return int(score)  
    
    