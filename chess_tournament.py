#! /usr/bin/env python3
# coding: utf-8
from tinydb import TinyDB, Query

NUMBER_OF_ROUND = 4

db = TinyDB('chess.json')


class Player:
    def __init__(self, name, first_name, sex, birth_date, ranking):
        self.name = name
        self.first_name = first_name
        self.birth_date = birth_date
        self.sex = sex
        self.ranking = ranking


class Tournament:
    def __init__(self, name, place, start_date, end_date, turn_number, list_player,
                 time_control, description):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.turn_number = turn_number
        self.round = round
        self.list_player = list_player
        self.time_control = time_control
        self.description = description


class Match:
    """ player pair with result for each"""

    def __init__(self, start_round, end_round):
        self.round = round
        self.start_round = start_round
        self.end_round = end_round

    def round(self):
        pass


class View:
    @staticmethod
    def welcome():
        print("bienvenue sur tournoi d'échec version 1")

    @staticmethod
    def choose_action():
        print("créer un joueur tapez  1")
        print("créer un tournoi tapez 2")
        print("changez un classement d'un joueur tapez 3")
        print("rentrez un résultat d'un match taper 4")
        print("afficher les rondes tapez 5")
        print("afficher un rapport taper 8")
        print("quitter taper 9")
        choice = input("votre choix : ")
        return choice

    @staticmethod
    def prompt_for_player_item():
        name = input("quelle est votre Nom : ").lower().capitalize()
        if name == "":
            return None
        first_name = input("quelle est votre prénom:").lower().capitalize()
        sex = input("sexe (masc, fem) :")
        # condition press m ou f
        birth_date = input("votre date de naissance:")
        # formatage
        ranking = input("votre classement : ")
        # condition +

        return name, first_name, sex, birth_date, ranking

    def pair(self):
        """ """
        pair = ()

    @staticmethod
    def prompt_create_tournament():
        """ """
        tournament_name = input("quelle est le nom du tournoi :").lower().capitalize()
        tournament_place = input("lieu :").lower().capitalize()
        tournament_start_date = input("date de début : ")
        # maintenant ou autre date
        tournament_end_date = input("date de fin : ")
        tournament_turn_number = NUMBER_OF_ROUND
        tournament_round = []
        tournament_list_player = []
        time_control = input("controle du temps (bullet, blitz, rapide) :")
        while time_control not in ['bullet', 'blitz', 'rapide']:
            time_control = input("controle du temps (bullet, blitz, rapide) :")

            if time_control not in ['bullet', 'blitz', 'rapide']:
                continue
        description = input("description :")
        return tournament_name, tournament_place, tournament_start_date, tournament_end_date, \
               tournament_turn_number, tournament_round, tournament_list_player, \
               time_control, description


class Controller:
    def __init__(self, view):
        # model
        self.players = []
        self.tournament = []

        # view
        self.view = view
        # controller

    def add_player(self, player_item):
        return self.players.append(Player(player_item[0], player_item[1], player_item[2],
                                          player_item[3], player_item[4]))

    def add_tournament(self, tourn_item):
        return self.tournament.append(Tournament(tourn_item[0], tourn_item[1], tourn_item[2],
                                                 tourn_item[3], tourn_item[4], tourn_item[5],
                                                 tourn_item[6], tourn_item[7]))

    def run(self):
        self.view.welcome()
        # load db in players
        run = True
        while run:
            choice = self.view.choose_action()
            if choice == '1':
                self.create_player()
            elif choice == '2':
                self.create_tournament()
            elif choice == '3':
                pass
            elif choice == '4':
                pass
            elif choice == '5':
                pass
            elif choice == '6':
                pass
            elif choice == '8':
                pass
            elif choice == '9':
                run = False
                if not run:
                    break

    def create_player(self):
        new_player = self.view.prompt_for_player_item()
        self.add_player(new_player)
        db.insert({'player name': new_player[0], 'player first_name': new_player[1],
                   'player sex': new_player[2], 'player birth_date': new_player[3], 'player ranking': new_player[4]})

    def create_tournament(self):
        new_tour = self.view.prompt_create_tournament()
        self.add_tournament(new_tour)
        db.insert({'tournament name': new_tour[0], 'tournament place': new_tour[1],
                   'tournament start date': new_tour[2], 'tournament end date': new_tour[3],
                   'tournament number turn': new_tour[4], 'tournament round': new_tour[5],
                   'tournament list player': new_tour[6], 'tournament time control': new_tour[7],
                   'tournament description': new_tour[8]})

        # def turn_result(self):
        pass

        # def tournament_result(self):
        pass

    def changing_player_ranking(self):
        pass


view = View()

controller = Controller(view)

controller.run()
