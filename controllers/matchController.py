from typing import Match
from views import tournament_view as view
class MatchController:
    
    def create_macth(self,list,round):
        match_player_one=list[0].name
        match_player_two=list[1].name
        match_score_player_one=list[0].score
        match_score_player_one+=self.__get_score_player_one("Enter score player one :")
        match_score_player_two=list[0].score
        match_score_player_two+=self.__get_score_player_two("Enter score player Two")
        match_register=([match_player_one,match_score_player_one][match_player_two,match_score_player_two])
        print (match_register)
        match=Match(match_player_one,match_player_two,match_score_player_one,match_score_player_two)
        round.matchs.append(match)
    @staticmethod
    def __get_score_player_one(message):
        score_player_one= view.get_input(message)
        while not score_player_one.isnumeric():
            score_player_one=view.get_input(f"Error: {message}")
        return int(score_player_one)
    @staticmethod
    def __get_score_player_two(message):
        score_player_two= view.get_input(message)
        while not score_player_two.isnumeric():
            score_player_two=view.get_input(f"Error: {message}")
        return int(score_player_two) 