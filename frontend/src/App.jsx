import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import './App.css';
import { useGame } from './context/GameContext';

function App() {
  const [data, setData] = useState("");
  const navigate = useNavigate();
  const { startGame } = useGame();

  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch("api/");
      const jsonData = await response.json();
      setData(jsonData.message);
    };

    fetchData();
  }, []);

  const handleStart = async () => {
      const data = await startGame();
      navigate(`/${data.phase}`);
  };

  return (
    <>
    <section id="center">
      <div>
          <h1>Welcome to Town of Salem 2 Simulator</h1>
      </div>
      <div>{data || "Loading..."}</div>
    </section>

    <button onClick={handleStart}>
      Start
    </button>
    
    <button onClick={() => navigate('rules')}>
      Rules
    </button>
    </>
  )
}

export default App
