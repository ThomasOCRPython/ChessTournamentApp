def enter_choice():
    choice = input("=======================================\n=                MENU                 =\n=======================================\n      Enter 1- Create new tournament\n      Enter 2- Reload tournament\n      Enter 3- view all tournaments\n      Enter 4- view all tournaments/rounds/matchs\n      Enter 5- view all players\n      Enter 6- change elo player\n      Enter 7- Quit\n=======================================\n      Enter your choice : ")
    return choice
def choice_tournament_reload():
    id_tournament=input("Enter id tournament : ")
    return id_tournament
def enter_new_elo():

    new_elo=input("give the new elo :")
    return new_elo
def get_message_sub_menu(message):
    choice=input(message)
    return choice 
def enter_select_sub_menu():
    select= input("=======================================================================\n                       CHOICE SUB MENU \n=======================================================================\n                1-display all players in a tournament\n                2-view all tournaments\n                3-back to menu\n\n                Enter your choice : ")
    return select
def update_player():
    id_player=input("choice id player:")
    return id_player
def print_player(player_id,player_name,player_elo):
    print("\t=============== PLAYER ID :",f"{player_id}","- NAME :",f"{player_name}"," ELO :",f"{player_elo}","===============")
def print_match_players(cpt,player_one,player_two) :
    print("=======================================================================\n                       MATCH",f"{cpt}","\n=======================================================================\n             MATCH :",f"{player_one}","=======VS======",f"{player_two}")
    
def print_tournaments_name(tournament_id,tournament_name):
    print("=======================================================================\n                       CHOICE TOURNAMENT ID:",f"{tournament_id}","\n=======================================================================\n=========== TOURNAMENT ID :",f"{tournament_id}",'=== TOURNAMENT NAME :', f"{tournament_name}","===========\n")
def print_rounds_name(round_name,round_id,date_time_start,date_time_end):
    print("=======================================================================\n                       CHOICE ROUND ID :",f"{round_id}","\n=======================================================================\n            Round_name :",f"{round_name}",   "***** Round_ID :",  f"{round_id}","*****","\nRound date_time_start:",f"{date_time_start}","\nRound date_time_end:",f"{date_time_end}")
def print_players_tournament(cpt,name,elo,score):
    print("=======================================================================\n                       PLAYER:",f"{cpt}","\n=======================================================================\n             PLAYER NAME :",f"{name}","\n             PLAYER ELO :",f"{elo}","\n             PLAYER SCORE :",f"{score}")
    

