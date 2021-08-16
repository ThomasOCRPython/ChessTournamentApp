from models.match import Match
from views import tournament_view as view
class MatchController:
    
    def create_match(self,player1,player2):
        match=Match(player1,player2)
        return match
        