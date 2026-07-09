import pytest
from models.game import Game
from models.player import Townie, Coven

class TestWinConditions:
    names = [
        'Player 1', 
        'Player 2', 
        'Player 3', 
        'Player 4', 
        'Player 5', 
        'Player 6', 
        'Player 7', 
        'Player 8', 
        'Player 9', 
        'Player 10', 
        'Player 11', 
        'Player 12', 
        'Player 13', 
        'Player 14', 
        'Player 15'
        ]

    @pytest.fixture
    def game(self):
        return Game(self.names)
    
    def test_game_has_default_attributes(self, game):

        assert len(game.dead_players) == 0
        assert len(game.living_players) == 15
        assert game.day == 1
        assert game.remaining_trials == 3
        assert game.winner == ""
        assert not game.is_over


    def test_all_players_have_default_attributes(self, game):
        for i in range(15):
            player = game.living_players[i]

            assert player.name == self.names[i]
            assert player.votes == 1
            assert player.defense == 0
            assert not player.blocked

            if isinstance(player, Townie):
                assert player.suspicion == 0.3
            else:
                assert player.suspicion == 0.4
    