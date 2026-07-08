import { useNavigate } from 'react-router-dom';
import { useGame } from '../src/context/GameContext';

const Day = () => {
  const { game, isGameOver, winner  } = useGame();
  const navigate = useNavigate();
  const { nextPhase } = useGame();
  
  const handleContinue = async () => {
      const data = await nextPhase();
      navigate(`/${data.phase}`);
  };
    
  return (
    <div className="game-container">
      <h1> {game.phase} {game.day}</h1>

       <div className="button-group">
        <button onClick={() => navigate('/')}>
          Back
        </button>

        <button onClick={handleContinue}>
          Continue
        </button>
       </div>
      </div>
    );
};

export default Day;