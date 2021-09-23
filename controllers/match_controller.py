from models.match import Match


class MatchController:
    def create_match(self, player1, player2):
        match = Match(player1, player2)
        return match
