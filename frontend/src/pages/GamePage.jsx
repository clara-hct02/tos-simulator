import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useGame } from '../context/GameContext';
import { DayUI } from '../phases/DayUI';
import { VotingUI } from '../phases/VotingUI';
import { JudgementUI } from '../phases/JudgementUI';
import { NightUI } from '../phases/NightUI';
import { WinUI } from '../phases/WinUI';

function GamePage() {
  const { game, nextPhase, resetGame } = useGame();
  const navigate = useNavigate();
  const [seenFinalPhase, setSeenFinalPhase] = useState(false);

  const handleContinue = () => {
    if (game.isOver && seenFinalPhase) {
      resetGame();
      navigate('/');
    } else if (game.isOver) {
      setSeenFinalPhase(true);
    } else {
      nextPhase();
    }
  };

  useEffect(() => {
    if (!game) {
      navigate('/');
    }
  }, [game, navigate]);

  if (!game) {
    return null;
  }

  const props = { game, onContinue: handleContinue};

  if (game.isOver && seenFinalPhase) {
    return (
      <WinUI
        game={game}
        onRestart={() => {
          setSeenFinalPhase(false);
          resetGame();
          navigate('/');
        }}
      />
    );
  }

  switch (game.phase.toLowerCase()) {
    case 'day':
      return <DayUI {...props} />;
    case 'voting':
      return <VotingUI {...props} />;
    case 'judgement':
      return <JudgementUI {...props} />;
    case 'night':
      return <NightUI {...props} />;
    default:
      return <p>Unknown phase: {game.phase}</p>;
  }
}

export default GamePage;
