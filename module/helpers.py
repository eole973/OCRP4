import datetime


def sort_rank_player(list_players):
    """order a list by rank ascending"""
    player_list_sort_rank = sorted(list_players, key=lambda x: x.rank)
    return player_list_sort_rank


def sort_alpha_player(list_players):
    """order a list by name ascending"""
    player_list_sort_rank = sorted(list_players, key=lambda x: x.name)
    return player_list_sort_rank


def convert_date(date):
    """convert a date to a readable sentence"""
    return date.strftime("%H:%M %d-%B-%Y")


def ask_birthday_check():
    """ask birthday and verify the answer"""
    date = input("votre date de naissance (jj/mm/aaaa) :")
    try:
        birth_date = datetime.datetime.strptime(date, "%d/%m/%Y")
    except ValueError:
        print("Désolé la date n'est pas valide, réessayez")
        return ask_birthday_check()
    return convert_date(birth_date)


def ask_gender():
    """ask the gender
    verify if in list
    transform to literal answer"""
    gender = input("genre taper m ou f (masc, fem) :").lower()
    while gender not in ['m', 'f']:
        gender = input("genre taper m ou f (masc, fem) :").lower()
    if gender == 'm':
        gender = 'masculin'
    elif gender == 'f':
        gender = 'feminin'
    return gender


def ask_rank():
    """ask the rank
    verify the input is a number"""
    number = input("votre classement : ")
    try:
        rank = int(number)
        if rank <= 0:
            print("le rang doit etre positif")
            ask_rank()
    except ValueError:
        print("un nombre est demandé.")
        return ask_rank()
    return rank


def ask_number_tournament():
    """ask the rank
        verify the input is a number"""
    choice = input("quelle est le numéro de tournoi: ")
    try:
        number = int(choice)
    except ValueError:
        print("un nombre est demandé.")
        return ask_number_tournament()
    return number


def ask_time_control():
    """ask time control and verify in a list"""
    time = input("controle du temps (bullet, blitz, rapide) :")
    while time not in ['bullet', 'blitz', 'rapide']:
        time = input("controle du temps (bullet, blitz, rapide) :")
        if time not in ['bullet', 'blitz', 'rapide']:
            continue
    return time


def ask_number_player():
    """ask the number
        verify the input is a number"""
    choice = input("choisir un numéro de joueur : ").lower()
    try:
        number = int(choice)
    except ValueError:
        print("un nombre est demandé.")
        return ask_number_player()
    return number


def add_to_check_player(pair, list_check):
    """add the number of the player
    who played against each other """
    for c in range(len(list_check)):
        if int(list_check[c][0]) == pair[0]:
            list_check[c] = list_check[c] + str(pair[4])
        if int(list_check[c][0]) == pair[4]:
            list_check[c] = list_check[c] + str(pair[0])
    return list_check
