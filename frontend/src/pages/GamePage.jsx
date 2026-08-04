import { useEffect } from 'react';
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

  useEffect(() => {
    if (!game) {
      navigate('/');
    }
  }, [game, navigate]);

  if (!game) {
    return null;
  }

  if (game.isOver) {
    return (
      <WinUI
        game={game}
        onRestart={() => {
          resetGame();
          navigate('/');
        }}
      />
    );
  }

  const props = { game, onContinue: nextPhase };

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
