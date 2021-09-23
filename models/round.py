import datetime


class Round:
    def __init__(self, round_name, date_time_start=None, date_time_end=None):
        self.round_name = round_name
        self.date_time_start = date_time_start
        self.date_time_end = date_time_end
        self.matchs = []

    def add_match(self, match):
        self.matchs.append(match)

    def datetime_end(self):
        self.date_time_end = datetime.datetime.now()

    def __str__(self):
        return f" round_name : {self.round_name} \n date_time_start : {self.date_time_start} \n date_time_end : {self.date_time_end} \n matchs : {self.matchs}"

    def serializer(self):
        data = {
            "round_name": self.round_name,
            "date_time_start": self.date_time_start.strftime("%A, %d %B,%Y"),
            "date_time_end": self.date_time_end.strftime("%A, %d %B,%Y"),
            "matchs": [match.match_serializer() for match in self.matchs],
        }
        return data
