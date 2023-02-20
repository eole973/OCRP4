class Player:
    """create player
    keep number of player"""
    number_of_player = 1

    def __init__(self, name=None, first_name=None, sex=None, birth_date=None, rank=None, score=None):
        self.num = Player.number_of_player
        self.name = name
        self.first_name = first_name
        self.birth_date = birth_date
        self.sex = sex
        self.rank = rank
        self.score = score
        Player.add_person()

    @classmethod
    def add_person(cls):
        """implement the number of player created"""
        cls.number_of_player += 1


class ListPlayer:
    """keep the information  of the player"""
    def __init__(self):
        self.player_list = []

    def add_player(self, player_t):
        """add info to the list"""
        self.player_list.append(player_t)


if __name__ == '__main__':
    player = Player()
    list_player = ListPlayer()
    list_player.add_player(player)
