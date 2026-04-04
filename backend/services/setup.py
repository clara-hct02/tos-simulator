import random 
from models import player

def setup_players():
    role_list = [player.Coven, player.Coven, player.Coven, player.Mayor, player.Cleric, player.Cleric,
        player.Tavern, player.Townie, player.Townie, player.Townie, player.Townie, player.Townie,
        player.Townie, player.Townie, player.Townie]
    
    players = []
    
    random.shuffle(role_list)

    for i in range(1, 16):
        new_player = role_list[i - 1](number=i)
        players.append(new_player)

    return players