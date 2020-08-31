def take_wand(player):
    """
    Request user and raise error if user count is not valid
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

def game(wand, player_one, player_two):
    """
        Base game process
    :param wand: count of wand for players
    :param player_one: name First player
    :param player_two: name Second player
    :return: None
    """
    print(f"We have {wand} wand")
    take = take_wand(player_one)  # User value
    wand -= take
    check = lambda wand: True if wand > 0 else False
    if check(wand):
        game(wand, player_two, player_one)  # Recursively function call if count of wand is not 0
    else:
        print(f"win {player_two}")


wand = 10
game(wand, 'Lis', 'Sisis')
    