import sys

from models.tournament import Tournament as tour
from models.player import Player as player
from controllers.tournament_controller import TournamentController as tournament
from views import home_menu_view as view, tournament_view
class HomeMenuController:
    


        
    def get_choice(self):

        self.choice = None
        while self.choice not in ("1", "2", "3","4","5","6","7"):
            self.choice = view.enter_choice()
            if(self.choice == "1"):
                tournament_controller=tournament()
                tournament_controller.create_new_tournament()
            elif(self.choice == "2"):
                self.__choice_tournament_and_reload()
            elif(self.choice =="3"):
                tour.table_tournament(self)
            elif(self.choice =="4"):
                self.__sub_menu()
            elif(self.choice =="5"):
                self.__show_players()
            elif(self.choice =="6"):
                self.__update_players_elo()
            elif(self.choice =="7"):
                self.__exit() 
            self.choice = None
    def __choice_tournament_and_reload(self):
        tour.table_tournament_not_finished(self)
        id_tournament=int(self.__get_id_tournament())
        table_tournament=tour.load_tournament_table(self,id_tournament)
        tournament_controller=tournament()
        tournament_controller.reload_tournament(table_tournament)
        tour.remove(self,id_tournament)

    def __sub_menu(self):
        self.select = int(view.enter_select_sub_menu())
        while self.select not in (1, 2, 3):
            self.select = int(view.enter_select_sub_menu())  
        if(self.select== 1):
            self.__order_players_tounrament()
        elif(self.select== 2):
            self.__select_round_and_match()
        else:
            pass   
    def __show_players(self):
        all_players=player.table_players(self)
        order_players=[]
        for player_not_order in all_players:
            order_players.append([player_not_order.doc_id,player_not_order["name"],player_not_order["elo"]])
            view.print_player(player_not_order.doc_id,player_not_order['name'],player_not_order['elo'])
        self.choice_order_players=int(view.get_message_sub_menu("\n\n\nChoose the order of presentation of the players:\n 1-alphabetic order\n 2-elo order\n 3-back to menu\n Enter your choice :"))
        while self.choice_order_players not in (1, 2, 3):
            self.choice_order_players=int(view.get_message_sub_menu("\n###wrong touch###\n\nChoose the order of presentation of the players:\n 1-alphabetic order\n 2-elo order\n 3-back to menu\n Enter your choice :"))
        if(self.choice_order_players==1):
            sorted_player=sorted(order_players, key=lambda player: player[1])
            for player_alpha in sorted_player:
                view.print_player(player_alpha[0],player_alpha[1],player_alpha[2])
        elif(self.choice_order_players==2):       
            sorted_player_elo=sorted(order_players, key=lambda player: int(player[2]))
            for player_elo in sorted_player_elo:
                view.print_player(player_elo[0],player_elo[1],player_elo[2])
        elif(self.choice_order_players==3):
            return
            
    def __update_players_elo(self):
        all_players=player.table_players(self)
        for player_not_order in all_players:
            view.print_player(player_not_order.doc_id,player_not_order['name'],player_not_order['elo'])
        id_player=int(view.update_player())
        print (id_player)
        new=(view.enter_new_elo())
        player_update=player.update_players_elo(self,new,id_player)
        print(player_update)

       
    def __get_id_tournament(self):
        id_tournament=view.choice_tournament_reload()
        while not id_tournament.isnumeric():
            id_tournament=view.choice_tournament_reload("Error")
        return id_tournament
    
    def __order_players_tounrament(self):
        tour.table_tournament(self)
        choice_id_tournament=int(view.get_message_sub_menu("choose the id of a tournament to see its players :"))
        tournament_player=tour.table_player_tournament(self,choice_id_tournament)
        order_tournament_player=[]
        for player_not_order in tournament_player: 
            order_tournament_player.append([player_not_order["name"],player_not_order["elo"],player_not_order["score"]])
            view.print_players_tournament(player_not_order['name'],player_not_order['elo'],player_not_order['score'])
        self.choice_order_player_tournament=int(view.get_message_sub_menu("Choose the order of presentation of the players:\n 1-alphabetic order\n 2-elo order\n 3-back to menu\n Enter your choice :"))
        while self.choice_order_player_tournament not in (1, 2, 3):
            self.choice_order_player_tournament=int(view.get_message_sub_menu("\n###wrong touch###\n\nChoose the order of presentation of the players:\n 1-alphabetic order\n 2-elo order\n 3-back to menu\n Enter your choice :"))
        if(self.choice_order_player_tournament==1):
            sorted_player_alpha=sorted(order_tournament_player, key=lambda player: player[0])
            for player_alpha in sorted_player_alpha:
                view.print_players_tournament(player_alpha[0],player_alpha[1],player_alpha[2])
        elif(self.choice_order_player_tournament==2):
            sorted_player_elo=sorted(order_tournament_player, key=lambda player: player[1])
            for player_alpha_b in sorted_player_elo:
                view.print_players_tournament(player_alpha_b[0],player_alpha_b[1],player_alpha_b[2])
        else:
            pass
    def __select_round_and_match(self):
        tour.table_tournament(self)
        choice_id_tournament=int(view.get_message_sub_menu("choose the id of a tournament to see its rounds :"))
        round_name=tour.table_round(self,choice_id_tournament)
        choice_id_round=int(view.get_message_sub_menu("choose the id of a round to see its matchs :"))
        tour.table_match(self,round_name,choice_id_round)



    def __exit(self):
        sys.exit()
    