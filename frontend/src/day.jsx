import { useNavigate } from 'react-router-dom';
import { useGame } from './context/GameContext'

const Day = () => {
  const { game } = useGame();
  const navigate = useNavigate();
    
  return (
    <div>
      <h1>Day {game.day}</h1>
        <button onClick={() => navigate('/')}>
          Back
        </button>

        <button onClick={() => navigate('')}>
          Continue
        </button>
      </div>
    );
};

export default Day;