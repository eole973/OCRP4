from datetime import datetime
from module.helpers import convert_date


class ListTournament:
    """keep the information  of the tournament"""
    def __init__(self):
        self.tournament_list = []

    def add_tournament(self, tournament):
        """add info to the list"""
        self.tournament_list.append(tournament)


class Tournament:
    """"create tournament """
    NUMBER_OF_ROUND = 4
    number_of_tournament = 1

    def __init__(self, name=None, place=None, start_date=None, time_control=None, description=None):
        self.num = Tournament.number_of_tournament
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = None
        self.turn_number = Tournament.NUMBER_OF_ROUND
        self.round_number = 1
        self.round_t = []
        self.list_player = []
        self.check_player_play = []
        self.time_control = time_control
        self.description = description
        Tournament.add_tournament()

    @classmethod
    def add_tournament(cls):
        """implement the number of tournament created"""
        cls.number_of_tournament += 1

    def add_end_tournament(self):
        """assign the date of end of tournament"""
        self.end_date = datetime.now()
        return convert_date(self.end_date)


class RoundTournament:
    """create a round  keep the result of the round"""
    def __init__(self, number):
        self.num = number
        self.result_player = []
        self.match_round = []


class Match:
    """ create match
    assign a name keep date of start, date of end
    """
    def __init__(self, name):
        self.name = name
        self.start_date_hour = None
        self.end_date_hour = None
        self.match_list = []


if __name__ == '__main__':
    t = Tournament()
