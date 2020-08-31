def game():
    """
        Base game process
    :return: None
    """
    wand, player_one, player_two = request_of_user()

    while True:
        wand = turn(wand, player_one, player_two)
        if not wand:
            break
        wand = turn(wand, player_two, player_one)
        if not wand:
            break


def request_of_user():
    """
    :return: Count of wand (int), First player name (str) and Second player name (str)
    """
    while True:
        try:
            wand = int(input("How many wands you want "))
            player_one = input("First player is: ")
            player_two = input("Second player is: ")
            if player_one.isdigit() or player_two.isdigit():
                raise ValueError
            return wand, player_one, player_two
        except ValueError:
            print("You entered incorrect data")



def turn(count_wand, first_player, second_player):
    """
        Players move process
    :param count_wand: the  value of the wands to be used
    :param first_player: Player whoes turn
    :param second_player: If first player is lose, second player win
    :return: False - if win second player or new count of wand
    """
    print(f"We have {count_wand} wand")
    take = take_wand(first_player)  # User value
    count_wand -= take
    check = lambda wand: True if wand > 0 else False
    if not check(count_wand):
        print(f"win {second_player}")
        return False
    else:
        return count_wand


def take_wand(player):
    """
        User request  and raise error if user count is not valid

    :param player:  active user
    :return: user input count
    """
    while True:
        try:
            take = int(input(f"{player}, how many wand you will take? "))
            if take <= 0:
                raise ValueError
            return take
        except ValueError:
            print("Please enter value the biggest then 0")
            continue


def restart_game():
    """
        Replay is request

    :return: True if yes
    """
    while True:
        answer = input("Do you wanna play again, y/n? ")
        if answer == 'y':
            return True
        elif answer == 'n':
            break

def run_game(func):
    """
        Game runner

    :param func: game function
    :return: None
    """
    while True:
        func()
        if not restart_game():
            break


wand = 10

run_game(game)
