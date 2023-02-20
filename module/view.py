#! /usr/bin/env python3
# coding: utf-8
import datetime
from module.helpers import convert_date, ask_rank, ask_gender, ask_number_tournament, ask_time_control, \
    ask_birthday_check


class View:
    """show information and get information """

    @staticmethod
    def welcome():
        print("------Bienvenue sur tournoi d'échec-------\n")

    @staticmethod
    def choose_action():
        """show the different action executable"""
        print("--------- Menu Principal---------")
        print("Pour gérer les joueurs \t\ttapez 1")
        print("Pour créer un tournoi \t\ttapez 2")
        print("Pour gérer les tournois \ttaper 3")
        print("Pour afficher un rapport \ttaper 4")
        print("Pour quitter \t\t\t\ttaper 9")
        choice = input("votre choix : ")
        return choice

    @staticmethod
    def player_choose_action():
        """show the different action for the player"""
        print("_________Menu Joueur_________")
        print("Pour créer un joueur \t\t\t\ttapez  1")
        print("Pour changer le classement d'un joueur \ttapez 2")
        print("Pour revenir aux menus principales \t\ttapez 9")
        choice = input("votre choix : ")
        return choice

    @staticmethod
    def tournament_choose_action():
        """show the different action for the progress of tournament"""
        print("########### Menu Tournoi ###########")
        print("Pour choisir les joueurs du tournoi \ttapez 1")
        print("Pour entrer les résultats d'une ronde \ttapez 2")
        print("Pour afficher le résultat \t\t\t\ttapez 3")
        print("Pour revenir aux menus principales \t\ttaper 9")
        choice = input("votre choix : ")
        return choice

    @staticmethod
    def report_choose_action():
        """show the different report executable"""
        print("********Menu Rapport***********")
        print("Pour voir la liste des joueurs par ordre alphabétique \t\t\t\ttapez 1")
        print("Pour voir la liste des joueurs par classement \t\t\t\t\t\ttapez 2")
        print("Pour voir la liste des joueurs d'un tournoi par ordre alphabétique \ttapez 3")
        print("Pour voir la liste des joueurs d'un tournoi par classement \t\t\ttapez 4")
        print("Pour voir la liste de tous les tournois \t\t\t\t\t\t\ttapez 5")
        print("Pour voir la liste de tous les tours d'un tournoi \t\t\t\t\ttapez 6")
        print("Pour voir la liste de tous les matchs d'un tournoi \t\t\t\t\ttapez 7")
        print("Pour revenir aux menux principales \t\t\t\t\t\t\t\t\ttaper 9")
        choice = input("votre choix : ")
        return choice

    @staticmethod
    def prompt_for_player_item():
        """ask items for the creation of a new player"""
        name = input("quelle est votre Nom : ").lower().capitalize()
        if name == "":
            return None
        first_name = input("quelle est votre prénom:").lower().capitalize()
        gender = ask_gender()
        birth_date = ask_birthday_check()
        rank = ask_rank()
        return name, first_name, gender, birth_date, rank

    @staticmethod
    def prompt_player(players_list):
        """show the list of player """
        for p in players_list:
            print(f"{p.num} \tnom: {p.name}  \t\tclassement : {p.rank} ")

    @staticmethod
    def prompt_change_rank():
        """ask the number id and the new rank"""
        num = int(input("ajuster le classement\nnuméro du joueur :"))
        rank = int(input("nouveau classement :"))
        return num, rank

    @staticmethod
    def prompt_create_tournament():
        """ask items for the creation of a new tournament """
        tournament_name = input("quelle est le nom du tournoi :").lower().capitalize()
        tournament_place = input("lieu :").lower().capitalize()
        tournament_start_date = input("date de début aujourd'hui tapez a  ou une autre date (HH:MN jj mm aaaa) : ")
        if tournament_start_date == 'a':
            tournament_start_date = convert_date(datetime.datetime.now())
        time_control = ask_time_control()
        description = input("description :")
        return tournament_name, tournament_place, tournament_start_date, time_control, description

    @staticmethod
    def show_list_tournament(tournament):
        """show the list of tournament saved"""
        print("voici la liste des tournois:")
        for t in tournament:
            print(f"{t.num} \tnom : {t.name} \tlieu : {t.place} date debut: {t.start_date} date de fin: {t.end_date} "
                  f"nombre de ronde :{t.round_number} ")

    @staticmethod
    def show_list_match(tournament):
        """show the list of match tournament saved"""
        for t in tournament:
            print(f"voici la liste des matchs du tournoi n° {t.num}: ")
            for r in t.round_t:
                print(f"RONDES {r.num} :")
                for m in r.match_round:
                    print(f"match début:{m.start_date_hour} fin: {m.end_date_hour}")
                    print(f"{m.match_list[1]} ({str(m.match_list[3])}, {str(m.match_list[2])}) vs "
                          f"{m.match_list[5]} ({str(m.match_list[7])}, {str(m.match_list[6])})")

    @staticmethod
    def show_list_round(tournament):
        """show the list of round tournament saved"""
        for t in tournament:
            print(f"voici la liste des rondes du tournoi n° {t.num}: ")
            for r in t.round_t:
                print(f"RONDES {r.num} :")
                for m in range(0, len(r.result_player), 4):
                    if r.result_player[m] == 'G':
                        print(f"{r.result_player[1 + m]} a gagné.")
                        print(f"{r.result_player[3 + m]} a perdu.")
                    elif r.result_player[m] == 'E':
                        print(f"{r.result_player[1 + m]} a fait match nul.")
                        print(f"{r.result_player[3 + m]} a fait match nul.")

    def request_tournament_number(self, tournament):
        """ask the saved number of a tournament"""
        self.show_list_tournament(tournament)
        request = ask_number_tournament()
        return request

    @staticmethod
    def show_pair(tournament_list, tournament_number):
        """show round pair with result previous match and rank"""
        for t in tournament_list:
            if t.num == tournament_number:
                for r in t.round_t:
                    if r.num == t.round_number:
                        print("############# ROUND " + str(r.num) + " ##############")
                        for m in r.match_round:
                            print(f"{m.match_list[1]} ( {str(m.match_list[3])}, {str(m.match_list[2])}) vs "
                                  f"{m.match_list[5]} ({str(m.match_list[7])}, {str(m.match_list[6])})")

    @staticmethod
    def ask_round_result():
        """ask if win or equal and the name """
        print("\npour les résultats par round ")
        print("indiquer G puis le nom du joueur pour le vainqueur")
        print("indiquer E puis le nom d'un joueur en cas d'égalité")

    @staticmethod
    def ask_result():
        """ask if the match is win or equal"""
        result = input("résultat:").capitalize()
        while result not in ['G', 'E']:
            result = input("résultat:").capitalize()
        return result

    @staticmethod
    def ask_name(tournament_list):
        """ask the name of the winning player
        or one if they are equal"""
        result_name = input("nom :").capitalize()
        while result_name not in [x.name for x in tournament_list]:
            result_name = input("nom :").capitalize()
        return result_name

    @staticmethod
    def show_tournament_result(tournament_list, tournament_number):
        """"show result of tournament
            sort  and shown the place the name and the count of match"""
        print("Voici les résultats du tournoi: ")
        for t in tournament_list:
            if t.num == tournament_number:
                tournament_result = sorted(sorted(t.list_player, key=lambda x: x.rank), key=lambda x: x.score,
                                           reverse=True)
                for p in tournament_result:
                    print(f"{p.name} - {p.score} - {p.rank}")

    @staticmethod
    def show_wrong_number_tournament():
        print('numéro de tournoi erroné')

    @staticmethod
    def show_already_pick_player():
        print("Vous avez déjà choisi les joueurs.")

    @staticmethod
    def show_add_player_before_get_result():
        print("Vous devez ajouter les joueurs avant rentrer un résultat.")

    @staticmethod
    def show_tournament_end_enable_to_add_result():
        print("Le tournoi est terminé.\n Vous ne pouvez plus rentrer de résultat.\n")

    @staticmethod
    def list_player_sorted_name():
        print("Liste de tous les joueurs par ordre alphabétique :")

    @staticmethod
    def list_player_sorted_rank():
        print("Liste de tous les joueurs par classement :")
