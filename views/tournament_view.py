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

def print_date_end_round(end):
     print("date end :::::::::::::::::::-->",end,"<--:::::::::::::::::::")