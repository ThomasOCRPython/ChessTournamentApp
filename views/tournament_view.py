def get_input(message):
    user_input=input(message)
    return user_input

def print_match_result(match):
    print(f"{match.player_one.name} : {match.score_player_one}", f"\n{match.player_two.name} : {match.score_player_two}")
    
def enter_score():
    score = input("================= SCORE ================\n      Enter score (1 / 2 / 0) : ")
    return score

def print_name_match_players(compte,match) :
    print("================ MATCH :",f"{compte}","================\n",match.player_one)
    print("------------------------------\n",match.player_two)
def print_round_name_and_date_time_start(round_name,name,round_date_time_start):
    print(round_name,"     ---","[ROUND :",f"{name}]","---","\ndate start :",round_date_time_start)
        
def print_date_end_round(end):
     print("date end :::::::::::::::::::-->",end,"<--:::::::::::::::::::")

def quit_and_save():
        quit=input("<<<<<<<<<< Do you want to stop and save the current tournament? >>>>>>>>> \n yes / no : ")
        return quit
        