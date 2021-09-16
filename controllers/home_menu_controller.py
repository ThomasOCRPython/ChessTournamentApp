import sys

from models.tournament import Tournament as tour
from models.player import Player as player
from controllers.tournament_controller import TournamentController as tournament
from views import home_menu_view as view, tournament_view
class HomeMenuController:
    


        
    def get_choice(self):

        self.choice = None
        while self.choice not in ("1", "2", "3","4","5","6","7","8"):
            self.choice = view.enter_choice()
            
            if(self.choice == "1"):
                tournament_controller=tournament()
                tournament_controller.create_new_tournament()
            elif(self.choice == "2"):
                self.__choice_tournament_and_reload()
            elif(self.choice =="3"):
                tour.table_tournament(self)
            elif(self.choice =="4"):
                tour.table_round(self)
            elif(self.choice =="5"):
                tour.table_match(self)
            elif(self.choice =="6"):
                player.table_players(self)
            elif(self.choice =="7"):
                new=(view.enter_new_elo())
                player.update_players_elo(self,new[0],new[1])
                print(new)
            else:
                self.__exit() 
            self.choice = None
    def __choice_tournament_and_reload(self):
        
       tour.table_tournament_not_finished(self)
       id_tournament=int(self.__get_id_tournament())
       table_tournament=tour.load_tournament_table(self,id_tournament)
       tournament_controller=tournament()
       tournament_controller.reload_tournament(table_tournament)
       tour.remove(self,id_tournament)

       
       
       
    
    def __get_id_tournament(self):
        id_tournament=view.choice_tournament_reload()
        while not id_tournament.isnumeric():
            id_tournament=view.choice_tournament_reload("Error")
        return id_tournament



    def __exit(self):
        sys.exit()
    