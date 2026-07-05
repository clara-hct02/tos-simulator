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
        return Game()

    @pytest.fixture
    def mock_game_state(self):
        game = Game(self.names)
        game.living_players = []
        game.dead_players = []
        return game
    
    def test_town_wins_when_all_coven_dead(self, mock_game_state):
        game = mock_game_state

        game.living_players = [
            Townie(number=1, name="Player 1"),
            Townie(number=2, name="Player 2")
        ]
        
        isOver = game.check_win()

        assert isOver
        assert game.is_over
        assert game.winner == "Town"
    
    def test_coven_wins_when_all_town_dead(self, mock_game_state):
        game = mock_game_state
        
        game.living_players = [
            Coven(number=1, name="Player 1"),
            Coven(number=2, name="Player 2"),
        ]
        
        isOver = game.check_win()

        assert isOver
        assert game.is_over
        assert game.winner == "Coven"
    

    def test_game_continues_when_both_teams_alive(self, mock_game_state):
        game = mock_game_state
        
        game.living_players = [
            Townie(number=1, name="Player 1"),
            Coven(number=2, name="Player 2"),
        ]
        
        isOver = game.check_win()

        assert not isOver
        assert not game.is_over
        assert game.winner == ""