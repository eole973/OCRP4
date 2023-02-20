from module.Player import Player


class ControllerPlayer:
    """create link between the controller and the player"""

    def __init__(self, view, lp):
        self.view = view
        self.lp = lp

    def run_player(self):
        """show different report for the program"""
        player_run = True
        while player_run:
            player_choice = self.view.player_choose_action()
            if player_choice == '1':
                self.create_player()
            if player_choice == '2':
                self.view.prompt_player(self.lp.player_list)
                num, new_rank = self.view.prompt_change_rank()
                self.adjust_rank(num, new_rank)
            elif player_choice == '9':
                player_run = False
                if not player_run:
                    break

    def create_player(self):
        """ ask information of  new player
        pass thought class player
        store them in a box"""
        p = self.view.prompt_for_player_item()
        new_player = Player(p[0], p[1], p[2], p[3], p[4])
        self.lp.add_player(new_player)

    def adjust_rank(self, num, new_rank):
        """save a new rank """
        for p in self.lp.player_list:
            if p.num == num:
                p.rank = new_rank
