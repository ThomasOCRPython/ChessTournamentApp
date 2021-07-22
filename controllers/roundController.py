class RoundController:
    nb_round=0
    def create_new_round:
        round_name=self.__get_round_name()
    @staticmethod
    def __get_round_name():
        name=print(f"Round {RoundController.nb_round}")
        return name