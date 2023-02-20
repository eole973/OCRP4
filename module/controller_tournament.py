import datetime
from module.Tournament import Match, Tournament, RoundTournament
from module.helpers import sort_alpha_player, ask_number_player, convert_date, add_to_check_player


class ControllerTournament:
    """create link between the controller and the tournament"""
    def __init__(self, view, lt, lp):
        self.view = view
        self.lt = lt
        self.lp = lp

    def run_tournament(self):
        """logic of the tournament"""
        tournament_run = True
        num = self.view.request_tournament_number(self.lt.tournament_list)
        for tour in self.lt.tournament_list:
            if num not in [x.num for x in self.lt.tournament_list]:
                self.view.show_wrong_number_tournament()
                break
            elif tour.num == num:
                while tournament_run:
                    tournament_choice = self.view.tournament_choose_action()
                    if tournament_choice == '1':
                        if len(tour.round_t) == 0:
                            self.view.prompt_player(sort_alpha_player(self.lp.player_list))
                            self.add_player_first_turn(num)
                            self.increment_score_in_player_list(num)
                            self.create_first_round_pair(num)
                            self.view.show_pair(self.lt.tournament_list, num)
                        else:
                            self.view.show_already_pick_player()

                    if tournament_choice == '2':
                        if len(tour.round_t) != 0:
                            if tour.round_number <= 4:
                                self.add_result_next_turn(num)
                                print(tour.check_player_play)
                                self.check_round_result(num)
                                tour.round_number += 1
                                if tour.round_number == 5:
                                    tour.end_date = convert_date(datetime.datetime.now())
                                    break
                                self.create_round_pair(num)
                                self.view.show_pair(self.lt.tournament_list, num)
                            else:
                                self.view.show_tournament_end_enable_to_add_result()
                        else:
                            self.view.show_add_player_before_get_result()

                    if tournament_choice == '3':
                        self.view.show_tournament_result(self.lt.tournament_list, num)

                    elif tournament_choice == '9':
                        tournament_run = False
                        if not tournament_run:
                            break

    def add_player_first_turn(self, tournament_number):
        """choose player with his number
        check if he's already in tournament player list
        add to tournament list """
        check_number_player = []
        for t in self.lt.tournament_list:
            if t.num == tournament_number:
                while len(t.list_player) < 8:
                    choice = ask_number_player()
                    for p in self.lp.player_list:
                        if choice in check_number_player:
                            break
                        if choice == p.num:
                            t.list_player.append(p)
                            check_number_player.append(choice)

    def create_first_round_pair(self, tournament_number):
        """create pair for first round with tourn player list
        sort tourn list  by rank (asc) and after by result
        divide list in two part
        pair first of each part etc."""
        for t in self.lt.tournament_list:
            if t.num == tournament_number:
                t.round_t = [RoundTournament(t.round_number)]
                for r in t.round_t:
                    if r.num == t.round_number:
                        tournament_list_sort = sorted(t.list_player, key=lambda x: x.rank)
                        length = len(tournament_list_sort)
                        middle_index = length // 2
                        first_half = tournament_list_sort[:middle_index]
                        second_half = tournament_list_sort[middle_index:]
                        for i in range(middle_index):
                            pair = [first_half[i].num, first_half[i].name, first_half[i].rank, first_half[i].score,
                                    second_half[i].num, second_half[i].name, second_half[i].rank, second_half[i].score]
                            match = Match(str(i + 1))
                            match.start_date_hour = convert_date(datetime.datetime.now())
                            match.match_list = pair
                            r.match_round.append(match)
                            t.check_player_play.append(str(first_half[i].num) + " " + str(second_half[i].num))
                            t.check_player_play.append(str(second_half[i].num) + " " + str(first_half[i].num))

    def create_round_pair(self, tournament_number):
        """create pair with tourn player
        sort tourn list by rank(asc) then by result(desc)
        associate first and second if they have already played with
        conbine first and third  etc."""
        for t in self.lt.tournament_list:
            if t.num == tournament_number:
                t.round_t.append(RoundTournament(t.round_number))
                for r in t.round_t:
                    if r.num == t.round_number:
                        tour_player_sorted = sorted(sorted(t.list_player, key=lambda x: x.rank), key=lambda x: x.score,
                                                    reverse=True)
                        for p in range(0, len(tour_player_sorted), 2):
                            pair = [tour_player_sorted[p].num, tour_player_sorted[p].name, tour_player_sorted[p].rank,
                                    tour_player_sorted[p].score, tour_player_sorted[p + 1].num,
                                    tour_player_sorted[p + 1].name, tour_player_sorted[p + 1].rank,
                                    tour_player_sorted[p + 1].score]
                            for i in range(len(tour_player_sorted)):
                                if tour_player_sorted[p].num == t.check_player_play[i][0] \
                                        and tour_player_sorted[p + 1].num in t.check_player_play[i][2:]:
                                    print(t.check_player_play[i][2:])
                                    pair = [tour_player_sorted[p].num, tour_player_sorted[p].name,
                                            tour_player_sorted[p].rank, tour_player_sorted[p].score,
                                            tour_player_sorted[p + 2].num, tour_player_sorted[p + 2].name,
                                            tour_player_sorted[p + 2].rank, tour_player_sorted[p + 2].score]
                            match = Match(str(p))
                            match.start_date_hour = convert_date(datetime.datetime.now())
                            match.match_list = pair
                            r.match_round.append(match)
                            t.check_player_play = add_to_check_player(pair, t.check_player_play)
                            print(t.check_player_play)

    def add_result_next_turn(self, tournament_number):
        """ get result of match in round
            check if player name is in tourm player list"""
        for t in self.lt.tournament_list:
            if t.num == tournament_number:
                for r in t.round_t:
                    if r.num == t.round_number:
                        self.view.ask_round_result()
                        counter_result = 0
                        while counter_result < Tournament.NUMBER_OF_ROUND:
                            result = self.view.ask_result()
                            result_name = self.view.ask_name(t.list_player)
                            if result == 'G':
                                for match in r.match_round:
                                    if result_name == match.match_list[1]:
                                        r.result_player.extend((result + " " + result_name).split())
                                        r.result_player.extend(('P' + " " + match.match_list[5]).split())
                                        match.end_date_hour = convert_date(datetime.datetime.now())
                                    elif result_name == match.match_list[5]:
                                        r.result_player.extend((result + " " + result_name).split())
                                        r.result_player.extend(('P' + " " + match.match_list[1]).split())
                                        match.end_date_hour = convert_date(datetime.datetime.now())
                            if result == 'E':
                                for match in r.match_round:
                                    if result_name == match.match_list[1]:
                                        r.result_player.extend((result + " " + result_name).split())
                                        r.result_player.extend(('E' + " " + match.match_list[5]).split())
                                        match.end_date_hour = convert_date(datetime.datetime.now())

                                    elif result_name == match.match_list[5]:
                                        r.result_player.extend((result + " " + result_name).split())
                                        r.result_player.extend(('E' + " " + match.match_list[1]).split())
                                        match.end_date_hour = convert_date(datetime.datetime.now())
                            counter_result = counter_result + 1

    def check_round_result(self, tournament_number):
        """verify in round result who win or equal
            and adjust their score"""
        for t in self.lt.tournament_list:
            if t.num == tournament_number:
                for r in t.round_t:
                    if r.num == t.round_number:
                        print(r.result_player)
                        for player in t.list_player:
                            for i in range(0, (len(t.list_player) * 2), 2):
                                if r.result_player[i] == 'G' and player.name == r.result_player[i + 1]:
                                    player.score += 1
                                if r.result_player[i] == 'E' and player.name == r.result_player[i + 1]:
                                    player.score += 0.5

    def increment_score_in_player_list(self, tournament_number):
        for t in self.lt.tournament_list:
            if t.num == tournament_number:
                for p in t.list_player:
                    p.score = 0.0
