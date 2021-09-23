from tinydb import TinyDB


class Player:
    def __init__(self, last_name, name, date_of_bird, sex, elo, score=0):
        self.last_name = last_name
        self.name = name
        self.date_of_bird = date_of_bird
        self.sex = sex
        self.elo = elo
        self.score = score
        # self.id=id
        self.oponents = []

    def add_oponent(self, oponent):
        self.oponents.append(oponent)

    def __str__(self):
        return f"last_name : {self.last_name} \n name : {self.name} \n date_of_bird : {self.date_of_bird} \n sex : {self.sex} \n elo : {self.elo} \n score : {self.score} \n oponent : {self.oponents}"

    def serializer(self):
        data = {
            "last_name": self.last_name,
            "name": self.name,
            "date_of_bird": self.date_of_bird,
            "sex": self.sex,
            "elo": self.elo,
            "score": self.score,
            "oponents": self.oponents,
        }
        return data

    def serializer_player(self):
        data = {
            "last_name": self.last_name,
            "name": self.name,
            "date_of_bird": self.date_of_bird,
            "elo": self.elo,
            "score": self.score,
        }
        return data

    def save(self):
        x = self.serializer_player()
        insert_compare = [x["last_name"], x["name"], x["date_of_bird"]]
        player_exist = self.player_exist()
        if insert_compare in player_exist:
            pass
        else:
            db = TinyDB("db.json", indent=4)
            player = db.table("player")
            player.insert(self.serializer_player())

    def table_players(self):
        # order_player=[]
        db = TinyDB("db.json", indent=4)
        player = db.table("player")
        all_players = player.all()
        return all_players

    def player_exist(self):
        exist_player = []
        db = TinyDB("db.json", indent=4)
        player = db.table("player")
        player_exist = player.all()
        for player in player_exist:
            exist_player.append(
                [player["last_name"], player["name"], player["date_of_bird"]]
            )
        return exist_player

    def update_players_elo(self, newElo, playerId):
        db = TinyDB("db.json", indent=4)
        players = db.table("player")
        players.update({"elo": newElo}, doc_ids=[playerId])
