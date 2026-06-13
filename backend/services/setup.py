import random 
from models import player

def setup_players(names):
    role_list = [player.Coven, player.Coven, player.Coven, player.Mayor, player.Cleric, player.Cleric,
        player.Tavern, player.Townie, player.Townie, player.Townie, player.Townie, player.Townie,
        player.Townie, player.Townie, player.Townie]
    
    players = []
    print(names)
    print("names")
    
    random.shuffle(role_list)

    for i in range(1, 16):
        new_player = role_list[i - 1](number=i, name=names[i - 1])
        players.append(new_player)

    return players