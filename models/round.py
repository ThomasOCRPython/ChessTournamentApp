class Round:
    def __init__(self, round_name, date_time_start, date_time_end):
        self.round_name=round_name
        self.date_time_start=date_time_start
        self.date_time_end=date_time_end
        self.matchs=[]
    #Quand on créera de rounds on créera des matchs    
    def add_match(self,match):
        self.matchs.append(match)    
    def add_list_of_match(self,list_of_match):
        self.list_of_match.append(list_of_match)
    
    def __str__(self):
        pass        