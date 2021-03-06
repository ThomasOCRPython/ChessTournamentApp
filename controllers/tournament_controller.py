from controllers.round_controller import RoundController
from controllers.match_controller import MatchController
from models.round import Round
from models.tournament import Tournament
from models.player import Player
from models.match import Match
from views import tournament_view as view
from controllers.player_controller import PlayerController
from datetime import datetime


class TournamentController:
    def __init__(self):
        self.tournament = None

    def create_new_tournament(self):

        tournament_name = self._get_name("Enter tournament name: ")
        tournament_place = self._get_place("Enter tournament place: ")
        tournament_date = (self._get_date("Enter the date of the tournament : "))
        tournament_get_time_control = self._get_time_control(
            "Enter '1' for 'bullet',\
             '2' for 'blits', '3' for 'coup rapide' :"
        )
        tournament_description = self._get_description("Enter description (if not press enter) :")

        self.tournament = Tournament(
            tournament_name,
            tournament_place,
            tournament_date,
            tournament_get_time_control,
            tournament_description,
        )

        self.player_controller = PlayerController()
        self.player_controller.create_player(self.tournament)

        self._create_round_one(self.tournament)
        if self._quit_and_save_the_round():
            return

        for nb in range(2, 2 + (int(self.tournament.nb_of_rounds) - 1)):
            self._create_other_round(nb, self.tournament)
            if self._quit_and_save_the_round():
                return

            if len(self.tournament.rounds) == (int(self.tournament.nb_of_rounds)):
                self.tournament.save()
                return

    @staticmethod
    def _get_name(message):
        name = view.get_input(message)
        while not name.isalpha():
            name = view.get_input(f"Error: {message}")
        return name

    @staticmethod
    def _get_place(message):
        place = view.get_input(message)
        while not place.isalpha():
            place = view.get_input(f"Error: {message}")
        return place

    @staticmethod
    def _get_date(message):
        get_date = view.get_input(message)
        while True:
            try:
                datetime.strptime(get_date, "%d/%m/%Y")
                break
            except ValueError:
                get_date = view.get_input(f"Error: {message}")
        return get_date

    @staticmethod
    def _get_time_control(message):
        time_control = view.get_input(message)
        while time_control not in ("1", "2", "3"):
            time_control = view.get_input(f"Error: {message}")
        if time_control == 1:
            time_control = "bullet"
        elif time_control == 2:
            time_control = "blitz"
        else:
            time_control = "coup rapide"
        return time_control

    @staticmethod
    def _get_description(message):
        description = view.get_input(message)
        return description

    def _get_handle_score(self):
        self.score = view.enter_score()
        while self.score not in ("1", "2", "0"):
            self.score = view.get_input("Error: Enter score (1 / 2 / 0): ")
        if self.score == "1":
            return 1, 0
        elif self.score == "2":
            return 0, 1
        else:
            return 0.5, 0.5

    def _quit_and_save_the_round(self):
        self.quit = view.quit_and_save().lower()
        while self.quit not in ("yes", "no"):
            self.quit = view.get_input("Error: Enter yes or no : ")
        if self.quit == "yes":
            self.tournament.save()
            return True
        elif self.quit == "no":
            return False

    def _create_round_one(self, tournament):
        compte = 0
        tournament.players.sort(key=lambda x: x.elo)
        sort_player = tournament.players
        round_controller = RoundController()
        round_controller.create_round(1, self.tournament)
        for i in range(int(len(sort_player) / 2)):
            matchController = MatchController()
            matchs = matchController.create_match(
                sort_player[i], sort_player[i + int(len(sort_player) / 2)]
            )
            sort_player[i].add_oponent(sort_player[i + int(len(sort_player) / 2)].name)
            sort_player[i + int(len(sort_player) / 2)].add_oponent(sort_player[i].name)
            round_controller.round.add_match(matchs)
        self._show_match_and_datetime_end(0, compte, round_controller)

    def _create_other_round(self, nb, tournament):
        incrm = 1
        compte = 0
        tournament.players.sort(key=lambda x: (-x.score, x.elo))
        sort_n_tournament = list(tournament.players)
        round_controller = RoundController()
        round_controller.create_round(nb, self.tournament)
        for _ in range(int(len(tournament.players) / 2)):
            matchController = MatchController()
            player1 = sort_n_tournament[0]
            player2 = sort_n_tournament[1]
            try:
                while player2.name in player1.oponents:
                    player2 = sort_n_tournament[1 + incrm]
                    incrm += 1
            except IndexError:
                player2 = sort_n_tournament[1]
            matchs = matchController.create_match(player1, player2)
            player1.add_oponent(player2.name)
            player2.add_oponent(player1.name)
            round_controller.round.add_match(matchs)
            sort_n_tournament.remove(player1)
            sort_n_tournament.remove(player2)

        self._show_match_and_datetime_end((nb - 1), compte, round_controller)

    def _show_match_and_datetime_end(self, indice, compte, round_controller):

        for match in self.tournament.rounds[indice].matchs:
            compte += 1
            view.print_name_match_players(compte, match)
            match.score_player_one, match.score_player_two = self._get_handle_score()
            match.update_score()
            view.print_match_result(match)

        round_controller.round.datetime_end()
        end = round_controller.round.date_time_end
        view.print_date_end_round(end)

    def reload_tournament(self, id_tournament):
        self.json = id_tournament
        self.tournament = None
        self.deserilizer()
        number_round_to_run = 4 - len(self.json["rounds"])
        if number_round_to_run == 4:
            self._create_round_one(self.tournament)

            for nb in range(2, 2 + (int(self.json["nb_of_rounds"]) - 1)):
                self._create_other_round(nb, self.tournament)
                if self._quit_and_save_the_round():
                    return
        else:
            for i in range(len(self.json["rounds"]) + 1, 5):
                self._create_other_round(i, self.tournament)
                if self._quit_and_save_the_round():
                    return
                if len(self.tournament.rounds) == (int(self.tournament.nb_of_rounds)):
                    self.tournament.save()
                    return

    def deserilizer(self):
        self.tournament = Tournament(
            self.json["name"],
            self.json["place"],
            self.json["date"],
            self.json["nb_of_rounds"],
        )
        self.tournament.players = []
        for player in self.json["players"]:
            reload_player = Player(
                player["last_name"],
                player["name"],
                player["date_of_bird"],
                player["sex"],
                player["elo"],
                player["score"],
            )
            reload_player.set_oponents(player["oponents"])
            self.tournament.add_player(reload_player)

        for round in self.json["rounds"]:
            reload_round = Round(
                round["round_name"],
                datetime.strptime(round["date_time_start"], "%A, %d %B,%Y"),
                datetime.strptime(round["date_time_end"], "%A, %d %B,%Y"),
            )
            for match in round["matchs"]:
                player1 = Player(
                    match["player_one"]["last_name"],
                    match["player_one"]["name"],
                    match["player_one"]["date_of_bird"],
                    match["player_one"]["sex"],
                    match["player_one"]["elo"],
                    match["player_one"]["score"],
                )
                player2 = Player(
                    match["player_two"]["last_name"],
                    match["player_two"]["name"],
                    match["player_two"]["date_of_bird"],
                    match["player_two"]["sex"],
                    match["player_two"]["elo"],
                    match["player_two"]["score"],
                )
                reload_match = Match(
                    player1,
                    player2,
                    match["score_player_one"],
                    match["score_player_two"],
                )
                reload_round.add_match(reload_match)
            self.tournament.add_round(reload_round)
