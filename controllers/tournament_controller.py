
from controllers.roundController import RoundController
from datetime import datetime
from controllers.matchController import MatchController
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
    
    
    A=[]
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
        self.__create_round_one(self.tournament)
        #for i in range(int(self.tournament.nb_of_rounds)-1):
           # self.__create_other_round(i,self.tournament)
        self.__create_other_round(self.tournament)
    
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

    def __create_round_one(self,tournament):
        compt=0
        tournament.players.sort(key = lambda x: x.elo)
        sort_player=tournament.players
        round_controller=RoundController()
        round_controller.create_round(1,self.tournament)
        for i in range(int(len(sort_player) / 2)):
            matchController=MatchController()
            matchs=matchController.create_match(sort_player[i], sort_player[i+int(len(sort_player) / 2)])
            sort_player[i].add_oponent(sort_player[i+int(len(sort_player) / 2)].name)
            sort_player[i+int(len(sort_player) / 2)].add_oponent(sort_player[i].name)
            round_controller.round.add_match(matchs)   
        for match in self.tournament.rounds[0].matchs:
            compt+=1
            print("================ MATCH :",f"{compt}","================\n",match.player_one)
            print("------------------------------\n",match.player_two)
            match.score_player_one, match.score_player_two = self.__get_handle_score()
            match.update_score()
            view.print_match_result(match)
        round_controller.round.datetime_end()
        end=round_controller.round.date_time_end
        print("date end :::::::::::::::::::-->",end,"<--:::::::::::::::::::")    
           
    
    def __create_other_round(self,tournament):
        incrm=1
        compte=0
        tournament.players.sort(key = lambda x: (-x.score,x.elo))
        sort_n_tournament=list(tournament.players)
        round_controller=RoundController()
        #round_controller.create_round(nb,self.tournament)
        round_controller.create_round(2,self.tournament)
        for i in range(int(len(tournament.players)/2)):
            matchController=MatchController()
            player1=sort_n_tournament[0]
            player2=sort_n_tournament[1]
            while player1.oponents==player2.name:
                     player2=sort_n_tournament[1+incrm]
            matchs=matchController.create_match(player1,player2)
            player1.add_oponent(player2.name)
            player2.add_oponent(player1.name)
            round_controller.round.add_match(matchs)
            sort_n_tournament.remove(player1)
            sort_n_tournament.remove(player2)   
        for match in self.tournament.rounds[1].matchs:
            compte+=1
            print("================ MATCH :",f"{compte}","================\n",match.player_one)
            print("------------------------------\n",match.player_two)
            match.score_player_one, match.score_player_two = self.__get_handle_score()
            match.update_score()
            view.print_match_result(match)
        round_controller.round.datetime_end()
        end=round_controller.round.date_time_end
        print("date end :::::::::::::::::::-->",end,"<--:::::::::::::::::::")
        
    def __get_handle_score(self):
        self.score = view.enter_score()
        while self.score not in ("1", "2", "0"):
            self.score=view.get_input(f"Error: Enter score (1 / 2 / 0): ")
        if(self.score == "1"):
            return 1,0
        elif(self.score == "2"):
            return 0,1
        else:
            return 0.5,0.5        
           



       
    

            
