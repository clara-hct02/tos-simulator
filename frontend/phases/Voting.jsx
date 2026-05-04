import { useNavigate } from 'react-router-dom';
import { useGame } from '../src/context/GameContext';

const Voting = () => {
  const { game } = useGame();
  const navigate = useNavigate();
  const { nextPhase } = useGame();
  
  const handleContinue = async () => {
      const data = await nextPhase();
      navigate(`/${data.phase}`);
  };
    
  return (
    <div>
      <h1> {game.phase} {game.day}</h1>
        {game.message}

        {game.events.map((event, i) => (
          <p key={i} className={event.type === "elimination" ? "text-red-500" : ""}>
            {event.text}
          </p>
        ))}

       <br></br>
        <button onClick={() => navigate('/')}>
          Back
        </button>

        <button onClick={handleContinue}>
          Continue
        </button>
      </div>
    );
};

export default Voting;