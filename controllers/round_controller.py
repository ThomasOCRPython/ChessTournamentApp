from views import tournament_view as view
from models.round import Round
from datetime import datetime


class RoundController:
    def __init__(self):
        pass

    def create_round(self, name, tournament_controller):
        round_name = "Round" + str(name)
        self.round = Round(round_name)
        self.round.date_time_start = datetime.now()
        tournament_controller.add_round(self.round)
        view.print_round_name_and_date_time_start(
            round_name, name, self.round.date_time_start
        )
