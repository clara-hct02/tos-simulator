import pytest
from models.game import Game
from models.player import Townie, Coven
from models.judgement_phase import JudgementPhase

class TestJudgementPhase:
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
        game.living_players = [
            Townie(name="Player 1", number=1),
            Coven(name="Player 2", number=2),
            Townie(name="Player 3", number=3),
            Townie(name="Player 4", number=4)
        ]
        player = game.living_players[0]
        game.phase = JudgementPhase(game, player)
        return game
    
    def test_pardoned_player_increase_suspicion(self, mock_game_state):
        game = mock_game_state
        phase = game.phase
        
        votes = [' voted innocent', ' voted guilty', ' voted innocent']
        initial_suspicion = phase.lynched.suspicion
        
        events = phase.get_events(game, vote_choices=votes)
        
        assert phase.lynched.suspicion == initial_suspicion + 0.1
        assert any("pardon" in event.text for event in events)
        assert phase.lynched in game.living_players


    def test_guilty_verdict_kills_player(self, mock_game_state):
        game = mock_game_state
        phase = game.phase
        
        votes = [' voted guilty', ' voted guilty', ' voted innocent']
        initial_suspicion = phase.lynched.suspicion
        
        events = phase.get_events(game, vote_choices=votes)
        
        assert phase.lynched.suspicion == initial_suspicion
        assert any("death" in event.text for event in events)
        assert not phase.lynched in game.living_players
        assert phase.lynched in game.dead_players

    