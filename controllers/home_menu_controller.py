import sys

from models.tournament import Tournament as tour

from controllers.tournament_controller import TournamentController as tournament
from views import home_menu_view as view, tournament_view
class HomeMenuController:
    


        
    def get_choice(self):

        self.choice = None
        while self.choice not in ("1", "2", "3"):
            self.choice = view.enter_choice()
            
            if(self.choice == "1"):
                tournament_controller=tournament()
                tournament_controller.create_new_tournament()
            elif(self.choice == "2"):
                self.__choice_tournament_and_reload()
            else:
                self.__exit() 
    
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
    