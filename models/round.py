class Round:
    def __init__(self, round_name, date_time_start, date_time_end):
        self.round_name=round_name
        self.date_time_start=date_time_start
        self.date_time_end=date_time_end
        self.matchs=[]
        #self.list_of_match=[]
        
    def add_match(self,match):
        self.matchs.append(match)    
    # def add_list_of_match(self,list_of_match):
    #     self.list_of_match.append(list_of_match)
    
    def __str__(self):
        return f" round_name : {self.round_name} \n date_time_start : {self.date_time_start} \n date_time_end : {self.date_time_start} \n matchs : {self.matchs}"   