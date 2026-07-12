import { useNavigate } from 'react-router-dom';
import { useGame } from '../src/context/GameContext';

const Win = () => {
  const { game } = useGame();
  const navigate = useNavigate();

    
  return (
    <div className="game-container">
      <h1> {game.winner} Wins!! </h1>

        <div className="button-group">
          <button onClick={() => navigate('/')}>
            Restart
          </button>

        </div>
      </div>
    );
};

export default Win;