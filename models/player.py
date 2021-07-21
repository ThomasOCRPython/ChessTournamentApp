class Player:
    def __init__(self, last_name, first_name, date_of_bird, sex,elo,score=0):
        self.last_name=last_name
        self.first_name=first_name
        self.date_of_bird=date_of_bird
        self.sex=sex
        self.elo=elo
        self.score=score

    def __str__(self):
        pass    