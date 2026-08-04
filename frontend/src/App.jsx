import { useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import './App.css';
import './names.css';
import { useGame } from './context/GameContext';

function App() {
  const navigate = useNavigate();
  const { startGame } = useGame();
  const inputRefs = useRef([]);

  const handleStart = async () => {
    const names = inputRefs.current.map((input, index) => 
      input.value || `Player ${index + 1}`
    );
    
    await startGame(names);
    navigate('/game');
  };

  return (
    <div className="game-container">
      <section id="center">
        <div>
            <h1>Welcome to Town of Salem 2 Simulator</h1>
        </div>
      </section>

      <div className="names-grid">
        {Array.from({ length: 15 }).map((_, index) => (
          <div key={index} className="name-input-group">
            <label>{index + 1}</label>
            <input
              ref={(el) => inputRefs.current[index] = el}
              type="text"
              placeholder={`Player ${index + 1}`}
            />
          </div>
        ))}
      </div>

      <div className="button-group">
        <button onClick={handleStart}>
          Start
        </button>
        
        <button onClick={() => navigate('rules')}>
          Rules
        </button>
      </div>
    </div>
  )
}

export default App
