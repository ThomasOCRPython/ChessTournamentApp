import sys
import os
from models.tournament import Tournament as tour
from models.player import Player as player
from controllers.tournament_controller import TournamentController as tournament
from views import home_menu_view as view


class HomeMenuController:
    def get_choice(self):
        self.choice = None
        while self.choice not in ("1", "2", "3", "4", "5", "6", "7"):
            os.system('clear')
            self.choice = view.enter_choice()
            if self.choice == "1":
                tournament_controller = tournament()
                tournament_controller.create_new_tournament()
            elif self.choice == "2":
                self._choice_tournament_and_reload()
            elif self.choice == "3":
                tour.table_tournament(self)
            elif self.choice == "4":
                self._sub_menu()
            elif self.choice == "5":
                self._show_players()
            elif self.choice == "6":
                self._update_players_elo()
            else:
                self.__exit()
            self.choice = None

    def _choice_tournament_and_reload(self):
        nb_tournament_id = tour.table_tournament_not_finished(self)
        if nb_tournament_id == []:
            return
        id_tournament = int(self._get_id_tournament())
        while id_tournament not in nb_tournament_id:
            id_tournament = int(self._get_id_tournament())
        table_tournament = tour.load_tournament_table(self, id_tournament)
        tournament_controller = tournament()
        tournament_controller.reload_tournament(table_tournament)
        tour.remove(self, id_tournament)

    def _sub_menu(self):
        self.select = view.enter_select_sub_menu()
        while self.select not in ("1", "2", "3"):
            self.select = view.enter_select_sub_menu()
        if self.select == "1":
            self._order_players_tournament()
        elif self.select == "2":
            self._select_round_and_match()
        else:
            pass

    def _show_players(self):
        all_players = player.table_players(self)
        if all_players == []:
            return
        order_players = []
        for player_not_order in all_players:
            order_players.append(
                [
                    player_not_order.doc_id,
                    player_not_order["name"],
                    player_not_order["elo"],
                ]
            )
            view.print_player(
                player_not_order.doc_id,
                player_not_order["name"],
                player_not_order["elo"],
            )
        self.choice_order_players = view.get_message_sub_menu(
            "\n\n\nChoose the order:\n 1-alphabetic \n 2-elo \n 3-back to menu\n Enter your choice :"
        )
        while self.choice_order_players not in ("1", "2", "3"):
            self.choice_order_players = view.get_message_sub_menu(
                "\n###wrong touch###\n\nChoose the order of presentation of the players:\
                \n 1-alphabetic order\n 2-elo order\n 3-back to menu\n Enter your choice :"
            )
        if self.choice_order_players == "1":
            sorted_player = sorted(order_players, key=lambda player: player[1])
            for player_alpha in sorted_player:
                view.print_player(player_alpha[0], player_alpha[1], player_alpha[2])
        elif self.choice_order_players == "2":
            sorted_player_elo = sorted(order_players, key=lambda player: int(player[2]))
            for player_elo in sorted_player_elo:
                view.print_player(player_elo[0], player_elo[1], player_elo[2])
        elif self.choice_order_players == "3":
            return

    def _update_players_elo(self):
        nb_id_player = []
        all_players = player.table_players(self)
        if all_players == []:
            return
        for player_not_order in all_players:
            view.print_player(
                player_not_order.doc_id,
                player_not_order["name"],
                player_not_order["elo"],
            )
            nb_id_player.append(player_not_order.doc_id)
        id_player = int(view.update_player())
        while id_player not in nb_id_player:
            id_player = int(view.update_player())
        new = view.enter_new_elo()
        while not new.isnumeric():
            new = view.enter_new_elo()
        player.update_players_elo(self, new, id_player)

    def _get_id_tournament(self):
        id_tournament = view.choice_tournament_reload()
        while not id_tournament.isnumeric():
            id_tournament = view.choice_tournament_reload("Error")
        return id_tournament

    def _order_players_tournament(self):
        nb_tournament_id = tour.table_tournament(self)
        if nb_tournament_id == []:
            return
        choice_id_tournament = int(
            view.get_message_sub_menu(
                "choose the id of a tournament to see its players :"
            )
        )
        while choice_id_tournament not in nb_tournament_id:
            choice_id_tournament = int(
                view.get_message_sub_menu(
                    "choose the id of a tournament to see its players :"
                )
            )
        tournament_player = tour.table_player_tournament(self, choice_id_tournament)
        order_tournament_player = []
        for player_not_order in tournament_player:
            order_tournament_player.append(
                [
                    player_not_order["name"],
                    player_not_order["elo"],
                    player_not_order["score"],
                ]
            )
            view.print_players_tournament(
                player_not_order["name"],
                player_not_order["elo"],
                player_not_order["score"],
            )
        self.choice_order_player_tournament = view.get_message_sub_menu(
            "Choose the order of presentation of the players:\n 1-alphabetic order\
                \n 2-elo order\n 3-back to menu\n Enter your choice :"
        )
        while self.choice_order_player_tournament not in ("1", "2", "3"):
            self.choice_order_player_tournament = view.get_message_sub_menu(
                "\n###wrong touch###\n\n\
                Choose the order of presentation of the players:\n 1-alphabetic order\n\
                     2-elo order\n 3-back to menu\n Enter your choice :"
            )
        if self.choice_order_player_tournament == "1":
            sorted_player_alpha = sorted(
                order_tournament_player, key=lambda player: player[0]
            )
            for player_alpha in sorted_player_alpha:
                view.print_players_tournament(
                    player_alpha[0], player_alpha[1], player_alpha[2]
                )
        elif self.choice_order_player_tournament == "2":
            sorted_player_elo = sorted(
                order_tournament_player, key=lambda player: player[1]
            )
            for player_alpha_b in sorted_player_elo:
                view.print_players_tournament(
                    player_alpha_b[0], player_alpha_b[1], player_alpha_b[2]
                )
        else:
            pass

    def _select_round_and_match(self):
        nb_tournament_id = tour.table_tournament(self)
        if nb_tournament_id == []:
            return
        choice_id_tournament = int(
            view.get_message_sub_menu(
                "choose the id of a tournament to see its rounds :"
            )
        )
        while choice_id_tournament not in nb_tournament_id:
            choice_id_tournament = int(
                view.get_message_sub_menu(
                    "choose the id of a tournament to see its rounds :"
                )
            )
        round_name = tour.table_round(self, choice_id_tournament)
        choice_id_round = int(
            view.get_message_sub_menu("choose the round id to see matchs :")
        )
        while choice_id_round not in round_name[1]:
            choice_id_round = int(
                view.get_message_sub_menu(
                    "choose the id of a round to see its matchs :"
                )
            )
        tour.table_match(self, round_name[0], choice_id_round)

    def __exit(self):
        sys.exit()
