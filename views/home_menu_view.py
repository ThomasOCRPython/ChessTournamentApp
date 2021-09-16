def enter_choice():
    choice = input("================= MENU ================\n      Enter 1- Create new tournament\n      Enter 2- Reload tournament\n      Enter 3- view all tournaments\n      Enter 4- view all rounds\n      Enter 5- view all matchs\n      Enter 6- view all players\n      Enter 7- change elo player\n      Enter 8- Quit\n Enter your choice : ")
    return choice
def choice_tournament_reload():
    id_tournament=input("Enter id tournament : ")
    return id_tournament
def enter_new_elo():
    player_id=input("give the player id :")
    new_elo=input("give the new elo :")
    return player_id,new_elo
   