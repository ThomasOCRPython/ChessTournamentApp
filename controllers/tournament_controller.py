from . import models
from models import tournament
from models.player import Player
from views.tournament_view import get_name, get_place, get_elo
#on peut créer fichier avec constantes
NUM_OF_PLAYER=8
class TournamentController:
    

    def __init__(self):
        self.tournament=None

    def crate_new_tournament(self):
        tournament_name=self.__get_name("Enter tournament name: ")
        tournament_place=self.__get_place("Enter tournament place: ")
        #création du modèle tournament
        self.tournament=Tournament(tournament_name,tournament_place)
        self.__create_player()
        self.__first_round()
    def __create_player(self):
        for i in range(NUM_OF_PLAYER):
            player_name=self.__get_name("Enter player name :  ")
            player_elo=self.__get_elo("Enter player Elo :  ")
            player = Player(player_name,player_elo)
            self.tournament.add_player(player)
    def __first_round(self):
        pass
    #round = Round("1")
    #for ...
        #round.add_match(match)
    #self.tournament.add_round(round)

    @staticmethod
    def __get_name(message):
        name=get_name(message)
        while not name.isalpha():
            name=get_name(f"Error: {message}")
        return name 
    @staticmethod
    def __get_place(message):
        place=get_place(message)
        while not place.isalpha():
            place=get_place(f"Error: {message}")
        return place 
    @staticmethod
    def __get_elo(message):
        elo=get_elo(message)
        while not elo.isnumeric():
            elo=get_elo(f"Error: {message}")
        return int(elo)    

if __name__=="__main__":
    tournamentController=TournamentController()
    tournamentController.crate_new_tournament()

