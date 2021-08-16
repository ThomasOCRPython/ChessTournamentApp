def get_input(message):
    user_input=input(message)
    return user_input
def print_match_result(match):
    print(f"{match.player_one.name} : {match.score_player_one}", f"\n{match.player_two.name} : {match.score_player_two}")
def enter_score():
    score = input("================= SCORE ================\n Enter score (1 / 2 / 0) : ")
    return score    