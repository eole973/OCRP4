from tinydb import TinyDB
from module.Player import Player
from module.Tournament import Tournament, RoundTournament, Match


class Db:
    """ save the player and the tournament
    in JSON via tiny DB"""
    def __init__(self):
        self.db = TinyDB('chess.json')
        self.players_table = self.db.table('players')
        self.tournament_table = self.db.table('tournament')

    def import_player(self, player_list):
        """retrieve the player info in the tiny DB
        and return player"""
        serialized_players = []
        for row in self.players_table:
            serialized_players.append(row)
        for player in serialized_players:
            name = player['name']
            first_name = player['first name']
            sex = player['sexe']
            birth_date = player['birth date']
            rank = player['rank']
            score = player['score']
            import_player = Player(name=name, first_name=first_name, sex=sex, birth_date=birth_date, rank=rank,
                                   score=score)
            player_list.append(import_player)

    def export_player(self, player_list):
        """catch player information and insert in tinyDB in JSON"""
        serialized_players = []
        for player in player_list:
            serialized_players.append({'name': player.name, 'first name': player.first_name, 'sexe': player.sex,
                                       'birth date': player.birth_date, 'rank': player.rank,
                                       'score': str(player.score)})
        self.players_table.truncate()
        self.players_table.insert_multiple(serialized_players)

    def import_tournament(self, tournament_list):
        """retrieve the tournament info in the tiny DB
                and return tournament"""
        serialized_tournament = []
        for row in self.tournament_table:
            serialized_tournament.append(row)
        for tournament in serialized_tournament:
            name = tournament['name']
            place = tournament['place']
            start_date = tournament['start date']
            end_date = tournament['end date']
            turn_number = tournament['turn number']
            round_number = tournament['round number']
            round_t_import = tournament['round tournament']
            list_player_import = tournament['list player']
            check_player_play = tournament['check_player_play']
            time_control = tournament['time control']
            description = tournament['description']
            import_tournament = Tournament(name=name, place=place, start_date=start_date,
                                           time_control=time_control, description=description)
            import_tournament.turn_number = turn_number
            import_tournament.round_number = round_number
            import_tournament.end_date = end_date
            serialized_rounds = []
            round_t = []
            for row in round_t_import:
                serialized_rounds.append(row)
            for r in serialized_rounds:
                num = r['round number']
                result_player = r['round result']
                import_match_round = r['round match']
                import_round = RoundTournament(num)
                import_round.result_player = result_player
                match_round = []
                for m in import_match_round:
                    name = m['match name']
                    start_date_hour = m['start date hour']
                    end_date_hour = m['end date hour']
                    match_list = m['match list']
                    import_match = Match(name)
                    import_match.start_date_hour = start_date_hour
                    import_match.end_date_hour = end_date_hour
                    import_match.match_list = match_list
                    match_round.append(import_match)
                import_round.match_round = match_round
                round_t.append(import_round)
            import_tournament.round_t = round_t
            serialized_players = []
            list_player = []
            for row in list_player_import:
                serialized_players.append(row)
            for player in serialized_players:
                name = player['name']
                first_name = player['first name']
                sex = player['sexe']
                birth_date = player['birth date']
                rank = player['rank']
                score = player['score']
                import_player = Player(name=name, first_name=first_name, sex=sex, birth_date=birth_date, rank=rank,
                                       score=score)
                list_player.append(import_player)
            import_tournament.list_player = list_player
            import_tournament.check_player_play = check_player_play
            tournament_list.append(import_tournament)

    def export_tournament(self, tournament_list):
        """export the player information and insert them in tinyDB in JSON"""
        serialized_tournament = []
        for tournament in tournament_list:
            serialized_players = []
            for player in tournament.list_player:
                serialized_players.append({'name': player.name, 'first name': player.first_name, 'sexe': player.sex,
                                           'birth date': player.birth_date, 'rank': player.rank,
                                           'score': str(player.score)})
            serialized_rounds = []
            for r in tournament.round_t:
                serialized_match = []
                for m in r.match_round:
                    serialized_match.append({'match name': m.name, 'start date hour': m.start_date_hour,
                                             'end date hour': m.end_date_hour, 'match list': m.match_list})
                serialized_rounds.append({'round number': r.num, 'round match': serialized_match,
                                          'round result': r.result_player})

            serialized_tournament.append({'name': tournament.name, 'place': tournament.place,
                                          'start date': tournament.start_date, 'end date': tournament.end_date,
                                          'turn number': tournament.turn_number,
                                          'round number': tournament.round_number,
                                          'round tournament': serialized_rounds,
                                          'list player': serialized_players,
                                          'check_player_play': tournament.check_player_play,
                                          'time control': tournament.time_control,
                                          'description': tournament.description})
        self.tournament_table.truncate()
        self.tournament_table.insert_multiple(serialized_tournament)
