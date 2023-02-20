from module.view import View
from module.Player import ListPlayer
from module.Tournament import Tournament, ListTournament
from module.helpers import sort_rank_player, sort_alpha_player
from module.dbcontext import Db
from module.controller_player import ControllerPlayer
from module.controller_tournament import ControllerTournament


class Controller:
    """create link between the different part of the program"""

    def __init__(self):
        self.view = View()
        self.lp = ListPlayer()
        self.lt = ListTournament()
        self.database = Db()
        self.controller_player = ControllerPlayer(self.view, self.lp)
        self.controller_tournament = ControllerTournament(self.view, self.lt, self.lp)

    def run(self):
        """logic of """
        self.view.welcome()
        self.database.import_player(self.lp.player_list)
        self.database.import_tournament(self.lt.tournament_list)

        run = True
        while run:
            choice = self.view.choose_action()
            if choice == '1':
                self.controller_player.run_player()
            if choice == '2':
                self.create_tournament()
            if choice == '3':
                self.controller_tournament.run_tournament()
            if choice == '4':
                self.rapport()
            elif choice == '9':
                self.database.export_player(self.lp.player_list)
                self.database.export_tournament(self.lt.tournament_list)
                run = False
                if not run:
                    break

    def create_tournament(self):
        """ ask information of  new tournament
        pass thought class tournament
        store them in a box"""
        t = self.view.prompt_create_tournament()
        new_tournament = Tournament(t[0], t[1], t[2], t[3], t[4])
        self.lt.add_tournament(new_tournament)

    def rapport(self):
        """show different report for the program"""
        report_run = True
        while report_run:
            report_choice = self.view.report_choose_action()
            if report_choice == '1':
                self.view.list_player_sorted_name()
                self.view.prompt_player(sort_alpha_player(self.lp.player_list))
            if report_choice == '2':
                self.view.list_player_sorted_rank()
                self.view.prompt_player(sort_rank_player(self.lp.player_list))
            if report_choice == '3':
                num2 = self.view.request_tournament_number(self.lt.tournament_list)
                for t in self.lt.tournament_list:
                    if num2 == t.num:
                        self.view.prompt_player(sort_alpha_player(t.list_player))
            if report_choice == '4':
                num3 = self.view.request_tournament_number(self.lt.tournament_list)
                for t in self.lt.tournament_list:
                    if num3 == t.num:
                        self.view.prompt_player(sort_rank_player(t.list_player))
            if report_choice == '5':
                self.view.show_list_tournament(self.lt.tournament_list)
            if report_choice == '6':
                num4 = self.view.request_tournament_number(self.lt.tournament_list)
                for t in self.lt.tournament_list:
                    if num4 == t.num:
                        self.view.show_list_round(self.lt.tournament_list)
            if report_choice == '7':
                num5 = self.view.request_tournament_number(self.lt.tournament_list)
                for t in self.lt.tournament_list:
                    if num5 == t.num:
                        self.view.show_list_match(self.lt.tournament_list)
            elif report_choice == '9':
                report_run = False
                if not report_run:
                    break


if __name__ == '__main__':
    controller = Controller()
    controller.run()
