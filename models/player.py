class Player:
    def __init__(self, last_name, name, date_of_bird, sex,elo,score=0):
        self.last_name=last_name
        self.name=name
        self.date_of_bird=date_of_bird
        self.sex=sex
        self.elo=elo
        self.score=score
        #self.id=id
        self.oponents=[]
    
    def add_oponent(self,oponent):
        self.oponents.append(oponent)

    def __str__(self):
        return f"last_name : {self.last_name} \n name : {self.name} \n date_of_bird : {self.date_of_bird} \n sex : {self.sex} \n elo : {self.elo} \n score : {self.score} \n oponent : {self.oponents}"
             