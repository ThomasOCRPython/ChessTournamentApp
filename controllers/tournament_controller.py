
from controllers.roundController import RoundController
from datetime import datetime 
from controllers.matchController import MatchController
from models.round import Round 
from models.tournament import Tournament
from models.player import Player
from models.match import Match
from views import tournament_view as view
from controllers.player_controller import PlayerController
from controllers.constantPlayer import NUM_OF_PLAYER


import datetime

class TournamentController:
    
    def __init__(self):
        self.tournament=None
    

    def create_new_tournament(self):
        
        tournament_name="Pegasus"#self.__get_name("Enter tournament name: ")
        tournament_place="kotte"#self.__get_place("Enter tournament place: ")
        tournament_date="30-07-2021"#self.__get_date("Enter the date of the tournament : ")
        tournament_get_time_control="1"#self.__get_time_control("Enter '1' for 'bullet', '2' for 'blits', '3' for 'coup rapide' :")
        # tournament_description=self.__get_description("Enter description")
        
        self.tournament=Tournament(tournament_name,tournament_place,tournament_date,tournament_get_time_control)
        self.player_controller=PlayerController()
        self.player_controller.create_player(self.tournament)
        #self.player_controller.player.add_player_bdd(self.tournament.players)
        
        
        
        test=self.tournament.table_tournament_not_finished()
        print(test)
        self.__create_round_one(self.tournament)
        if self.__quit_and_save_the_round():
            return 
        
        
        for nb in range(2,2+(int(self.tournament.nb_of_rounds)-1)):
            self.__create_other_round(nb,self.tournament)
            if self.__quit_and_save_the_round():
                return 
        
        

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

    def __quit_and_save_the_round(self):
        self.quit = view.quit_and_save().lower()
        while self.quit not in ("yes", "no"):
            self.quit=view.get_input(f"Error: Enter yes or no : ")
        if(self.quit == "yes"):
            self.tournament.save()
            return True
        elif(self.quit == "no"):
            return False
    

    def __create_round_one(self,tournament):
        compte=0
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
            compte+=1
            view.print_name_match_players(compte,match)
            match.score_player_one, match.score_player_two = self.__get_handle_score()
            match.update_score()
            view.print_match_result(match)
        round_controller.round.datetime_end()
        end=round_controller.round.date_time_end
        view.print_date_end_round(end)
        
                    
    def __create_other_round(self,nb,tournament):
        incrm=1
        compte=0
        tournament.players.sort(key = lambda x: (-x.score,x.elo))
        sort_n_tournament=list(tournament.players)
        round_controller=RoundController()
        round_controller.create_round(nb,self.tournament)
        for _ in range(int(len(tournament.players)/2)):
            matchController=MatchController()
            player1=sort_n_tournament[0]
            player2=sort_n_tournament[1]
            try:
                while player2.name in player1.oponents:
                        player2=sort_n_tournament[1+incrm]
                        incrm+=1
            except IndexError:
                player2=sort_n_tournament[1]                    
            matchs=matchController.create_match(player1,player2)
            player1.add_oponent(player2.name)
            player2.add_oponent(player1.name)
            round_controller.round.add_match(matchs)
            sort_n_tournament.remove(player1)
            sort_n_tournament.remove(player2)  
        print (nb)    
        for match in self.tournament.rounds[nb-1].matchs:
            
            compte+=1
            view.print_name_match_players(compte,match)
            match.score_player_one, match.score_player_two = self.__get_handle_score()
            match.update_score()
            view.print_match_result(match)
        
        round_controller.round.datetime_end()
        end=round_controller.round.date_time_end
        view.print_date_end_round(end)
        

    
    def reload_tournament(self,id_tournament):
        print('coucou')
        
        
        self.json=id_tournament
        
        # self.json=self.tournament.load_tournament_table(id_tournament)
        self.tournament = None # je met none car dans le cas normal il serait à None.
        #Il va aller lire le json et récupérer l'information du tournoi qu'on veut reprendre (Dans notre exemple self.json)
                           
        self.deserilizer()
        
        
        number_round_to_run = 4 - len(self.json["rounds"])
        print(number_round_to_run)
        
        if number_round_to_run == 4:
            self.__create_round_one(self.tournament)
            for nb in range(2,2+(int(self.tournament.nb_of_rounds)-1)):
                self.__create_other_round(nb,self.tournament)
                if self.__quit_and_save_the_round():
                    return
        else:
            
            for i in range(len(self.json["rounds"]) + 1, 5):
                
                self.__create_other_round(i,self.tournament)
                if self.__quit_and_save_the_round():
                    return
                #pass
                #run_round(i)

    def deserilizer(self):
        self.tournament = Tournament(self.json["name"], self.json["place"],self.json["date"],self.json["nb_of_rounds"])
        self.tournament.players = []  
        for player in self.json["players"]:
            reload_player = Player(player["last_name"],player["name"],player["date_of_bird"], player["sex"], player["elo"], player["score"])
            self.tournament.add_player(reload_player)
          
        for round in self.json["rounds"]:
            reload_round = Round(round["round_name"],datetime.datetime.strptime(round["date_time_start"],'%A, %d %B,%Y'),datetime.datetime.strptime(round["date_time_end"],'%A, %d %B,%Y'))
            for match in round["matchs"]:
                player1 = Player(match["player_one"]["last_name"],match["player_one"]["name"],match["player_one"]["date_of_bird"],match["player_one"]["sex"],match["player_one"]["elo"], match["player_one"]["score"])
                player2 = Player(match["player_two"]["last_name"],match["player_two"]["name"],match["player_two"]["date_of_bird"],match["player_two"]["sex"],match["player_two"]["elo"], match["player_two"]["score"])             
                reload_match = Match(player1, player2, match["score_player_one"], match["score_player_two"])
                reload_round.add_match(reload_match)
            self.tournament.add_round(reload_round)
       
        

    
        
        
    



       
    

            
