import { useNavigate } from 'react-router-dom';
import { useGame } from '../src/context/GameContext';

const Judgement = () => {
  const { game } = useGame();
  const navigate = useNavigate();
  const { nextPhase } = useGame();
  
  const handleContinue = async () => {
      const data = await nextPhase();
      navigate(`/${data.phase}`);
  };
    
  return (
    <div className="game-container">
      <h1> {game.phase} {game.day}</h1>
        {game.message}

        <div className="events-container">
          {game.events.map((event, i) => (
            <div key={i} className={`event ${event.type === "judgement" ? "judgement" : ""}`}>
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