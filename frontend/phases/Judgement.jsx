import { useNavigate } from 'react-router-dom';
import { useGame } from '../src/context/GameContext';
import { useEffect } from 'react';

const Judgement = () => {
  const { game, isGameOver, winner  } = useGame();
  const navigate = useNavigate();
  const { nextPhase } = useGame();
  
  const handleContinue = async () => {
      const data = await nextPhase();
      navigate(`/${data.phase}`);
  };

  useEffect(() => {
        if (isGameOver) {
          console.log("game over");
          navigate(`/Win`);
        }
      }, [isGameOver, winner, navigate]);
    
  return (
    <div className="game-container">
      <h1> {game.phase} {game.day}</h1>

        <div className="events-container">
          {game.events.map((event, i) => (
            <div key={i} className="event">
              <p>{event.text}</p>
            </div>
          ))}
        </div>

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

export default Judgement;