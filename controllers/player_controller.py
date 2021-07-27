
from models.tournament import Tournament
from controllers import constantPlayer as const
from views import tournament_view as view
from models.player import Player
from datetime import datetime




class PlayerController:


    def create_player(self, tournament_controller):
        for i in range(const.NUM_OF_PLAYER):
            player_last_name=self.__get_last_name("Enter player last name : ")
            player_name=self.__get_name("Enter player first name : ")
            player_date_of_bird=self.__get_date_of_bird("Enter player date of bird : ")
            player_sex=self.__get_sex("Enter sex player 'M' for male, 'F'for female 'N'for none: ")
            player_elo=self.__get_elo("Enter player Elo : ")
            player_score=self.__get_score("Enter score player : ")
            player =Player(player_last_name,player_name,player_date_of_bird,player_sex, player_elo)
            tournament_controller.add_player(player)

    @staticmethod
    def __get_name(message):
        name=view.get_name(message)
        while not name.isalpha():
            name=view.get_name(f"Error: {message}")
        return name 
    @staticmethod
    def __get_elo(message):
        elo= view.get_elo(message)
        while not elo.isnumeric():
            elo=view.get_elo(f"Error: {message}")
        return int(elo) 
    @staticmethod
    def __get_last_name(message):
        last_name= view.get_last_name(message)
        while not last_name.isalpha():
            last_name=view.get_last_name(f"Error: {message}")
        return last_name    
    @staticmethod
    def __get_date_of_bird(message):
        get_date_of_bird= view.get_input(message)
        while True:
            try:

                datetime.strptime(get_date_of_bird, '%d/%m/%Y')
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
    
    