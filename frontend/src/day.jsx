import { useNavigate } from 'react-router-dom';
import { useGame } from './context/GameContext';

const Day = () => {
  const { game } = useGame();
  const navigate = useNavigate();

  console.log(game);
    
  return (
    <div>
      <h1>Day {game.day}</h1>
        {game.message}

       <br></br>
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