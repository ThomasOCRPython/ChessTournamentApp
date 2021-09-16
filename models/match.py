class Match:
    def __init__(self, player_one, player_two, score_player_one=0, score_player_two=0):
        self.player_one=player_one
        self.player_two=player_two
        self.score_player_one=score_player_one
        self.score_player_two=score_player_two

    def update_score(self,):
        self.player_one.score += self.score_player_one
        self.player_two.score += self.score_player_two   

    def __str__(self):
        return f"player_one: {self.player_one} \n player_two :{self.player_two} \n score_player_one ={self.score_player_one}\n score_player_two ={self.score_player_two}"    
    
    def match_serializer(self):
        data = {"player_one" : self.player_one.serializer(),
                "player_two" : self.player_two.serializer(),
                "score_player_one" : self.score_player_one,
                "score_player_two" : self.score_player_two}
        return data
    
    def add_match_bdd ( self , match_bdd ):
        pass